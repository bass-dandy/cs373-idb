var app = angular
    .module('meccaApp', ['ngRoute', 'ngAnimate'])
    .factory("Sources", function($http) {
        return {
            fromUri: function(uri) {
                return $http.get("http://downing.club" + uri);
            }
        }
    })
    .filter('millisToMinutes', function() {
        return function(input) {
            var minutes = Math.floor(input / 1000 / 60);
            var seconds = Math.floor(input / 1000 % 60);
            if(seconds < 10) {
                seconds = '0' + seconds;
            }
            return minutes + ':' + seconds;
        };
    })
    .filter('startFrom', function() {
        return function(input, start) {
            start = +start;
            return input.slice(start);
        };
    });

app.controller('mainController', function($scope) {
    $scope.order = "name";

    $scope.setOrder = function(order) {
        $scope.order = order;
    }
});

app.controller('aboutController', function($scope, $http, Sources) {
    // Register function for running unit tests
    $scope.runTests = function() {
        Sources.fromUri("/api/runtests")
            .then(function(response) {
                $scope.test = response.data;
            }, function() {});
    }
    // Get Github commit stats
    $scope.commits = 0;
    $http.get("https://api.github.com/repos/naughtyfiddle/cs373-idb/stats/contributors")
        .then(function(response) {
            response.data.forEach(function(entry) {
                $scope[entry.author.login] = {};
                $scope[entry.author.login].commits = entry.total;
                $scope.commits += entry.total;
                $scope[entry.author.login].issues = 0;
            });
        }, function() {});
    // Get Github issue stats
    $scope.issues = 0;
    $http.get("https://api.github.com/repos/naughtyfiddle/cs373-idb/issues?state=all&per_page=100")
        .then(function(response) {
            response.data.forEach(function(entry) {
                $scope[entry.user.login].issues++;
                $scope.issues++;
            });
        }, function() {});
});

app.controller('artistsController', function($scope, Sources) {
    $scope.modelType = 'artists'; 
    Sources.fromUri("/api/artists")
        .then(function(response) {
            $scope.currentPage = 0;
            $scope.pageSize = 12;
            $scope.numberOfPages=function(){
                return Math.ceil($scope.models.length/$scope.pageSize);                
            };
            $scope.models = response.data;
        }, function() {});
});

app.controller('labelsController', function($scope, Sources) {
    $scope.modelType = 'labels'; 
    Sources.fromUri("/api/labels")
        .then(function(response) {
            $scope.currentPage = 0;
            $scope.pageSize = 12;
            $scope.numberOfPages=function(){
                return Math.ceil($scope.models.length/$scope.pageSize);                
            };
            $scope.models = response.data;
        }, function() {});
});

app.controller('releasesController', function($scope, Sources) {
    $scope.modelType = 'releases'; 
    Sources.fromUri("/api/releases")
        .then(function(response) {
            $scope.currentPage = 0;
            $scope.pageSize = 12;
            $scope.numberOfPages = function() {
                return Math.ceil($scope.models.length/$scope.pageSize);                
            };
            $scope.models = response.data;
        }, function() {});
});

app.config(function($routeProvider, $locationProvider, $animateProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'templates/splash.html',
            controller  : 'mainController'
        })

        .when('/about', {
            templateUrl : 'templates/about.html',
            controller  : 'aboutController'
        })

        .when('/artists', {
            templateUrl : 'templates/models.html',
            controller  : 'artistsController'
        })

        .when('/labels', {
            templateUrl : 'templates/models.html',
            controller  : 'labelsController'
        })

        .when('/releases', {
            templateUrl : 'templates/models.html',
            controller  : 'releasesController'
        })

        .when('/labels/:id', {
            templateUrl : 'templates/label.html',
            controller  : 'mainController'
        })

        .when('/artists/:id', {
            templateUrl : 'templates/artist.html',
            controller  : 'mainController'
        })

        .when('/releases/:id', {
            templateUrl : 'templates/release.html',
            controller  : 'mainController'
        });

    $locationProvider.html5Mode(true);
    $animateProvider.classNameFilter(/^(?:(?!ng-animate-disabled).)*$/);
});

app.controller('artistController', function($scope, $routeParams, Sources) {
    // For selecting a random album cover
    $scope.random = function(length) {
        return Math.floor(Math.random() * length);
    };
    // Get artist data
    Sources.fromUri("/api/artists/" + $routeParams.id)
        .then(function(response) {
            $scope.artist = response.data;

            // Get release data
            var releases = [];
            response.data.releases.forEach(function(entry) {
                Sources.fromUri(entry.uri)
                    .then(function(response2) {
                        releases.push(response2.data);
                    }, function() {});
            });
            $scope.artist.releases = releases;

            // Get label data
            Sources.fromUri(response.data.primaryLabel.uri)
                    .then(function(response2) {
                        $scope.artist.label = response2.data;
                    }, function() {});
        }, function() {});
});

app.controller('labelController', function($scope, $routeParams, Sources) {
    Sources.fromUri("/api/labels/" + $routeParams.id)
        .then(function(response) {
            $scope.label = response.data;

            // Get artist data
            var artists = [];
            response.data.artists.forEach(function(entry) {
                Sources.fromUri(entry.uri)
                    .then(function(response2) {
                        artists.push(response2.data);
                    }, function() {});
            });
            $scope.label.artists = artists;
        }, function() {});
});

app.controller('releaseController', function($scope, $routeParams, Sources) {
    Sources.fromUri("/api/releases/" + $routeParams.id)
        .then(function(response) {
            $scope.release = response.data;

            // Get song data
            var songs = [];
            response.data.songs.forEach(function(entry) {
                Sources.fromUri(entry.uri)
                    .then(function(response2) {
                        songs.push(response2.data);
                    }, function() {});
            });
            $scope.release.songs = songs;

            // Get artist data
            Sources.fromUri(response.data.artists[0].uri)
                .then(function(response2) {
                    $scope.release.artist = response2.data;
                }, function() {});
        }, function() {});
});
