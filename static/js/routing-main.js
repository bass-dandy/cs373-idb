var app = angular
    .module('meccaApp', ['ngRoute', 'ngAnimate'])
    .factory("Sources", function($http) {
        return {
            fromUri: function(uri) {
                return $http.get("http://downing.club" + uri);
            }
        }
    });

app.controller('mainController', function($scope) {
    $scope.order = "name";

    $scope.setOrder = function(order) {
        $scope.order = order;
    }
});

app.controller('aboutController', function($scope, Sources) {
    $scope.runTests = function() {
        Sources.fromUri("/api/runtests")
            .then(function(response) {
                $scope.test = response.data;
            }, function() {});
    }
});

app.controller('artistsController', function($scope, Sources) {
    $scope.modelType = 'artists'; 
    Sources.fromUri("/api/artists")
        .then(function(response) {
            $scope.models = response.data;
        }, function() {});
});

app.controller('labelsController', function($scope, Sources) {
    $scope.modelType = 'labels'; 
    Sources.fromUri("/api/labels")
        .then(function(response) {
            $scope.models = response.data;
        }, function() {});
});

app.controller('releasesController', function($scope, Sources) {
    $scope.modelType = 'releases'; 
    Sources.fromUri("/api/releases")
        .then(function(response) {
            $scope.models = response.data;
        }, function() {});
});

app.config(function($routeProvider, $locationProvider) {
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
});

app.controller('artistController', function($scope, $routeParams, Sources) {
    Sources.fromUri("/api/artists/" + $routeParams.id)
        .then(function(response) {
            $scope.artist = response.data;
            var releases = [];
            response.data.releases.forEach(function(entry) {
                Sources.fromUri(entry.uri)
                    .then(function(response2) {
                        releases.push(response2.data);
                    }, function() {});
            });
            $scope.artist.releases = releases;
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
            var songs = [];
            response.data.songs.forEach(function(entry) {
                Sources.fromUri(entry.uri)
                    .then(function(response2) {
                        songs.push(response2.data);
                    }, function() {});
            });
            $scope.release.songs = songs;
        }, function() {});
});
