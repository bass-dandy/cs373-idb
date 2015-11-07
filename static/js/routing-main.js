var app = angular.module('meccaApp', ['ngRoute', 'ngAnimate']);

app.controller('mainController', function($scope) {});

app.controller('artistsController', function($scope, $http) {
    $scope.modelType = 'artists'; 
    $http.get("http://downing.club/api/artists")
        .then(function(response) {
            $scope.models = response.data;
            console.log(response.data);
        }, function() {
            console.log("Failed to retrieve artists");
        });
});

app.controller('labelsController', function($scope, $http) {
    $scope.modelType = 'labels'; 
    $http.get("http://downing.club/api/labels")
        .then(function(response) {
            $scope.models = response.data;
            console.log(response.data);
        }, function() {
            console.log("Failed to retrieve labels");
        });
});

app.controller('releasesController', function($scope, $http) {
    $scope.modelType = 'releases'; 
    $http.get("http://downing.club/api/releases")
        .then(function(response) {
            $scope.models = response.data;
            console.log(response.data);
        }, function() {
            console.log("Failed to retrieve releases");
        });
});

app.config(function($routeProvider, $locationProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'templates/splash.html',
            controller  : 'mainController'
        })

        .when('/about', {
            templateUrl : 'templates/about.html',
            controller  : 'mainController'
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

app.controller('artistController', function($scope, $http, $routeParams) {
    $http.get("http://downing.club/api/artists/" + $routeParams.id)
        .then(function(response) {
            $scope.artist = response.data;
            var releases = [];
            response.data.releases.forEach(function(entry) {
                $http.get("http://downing.club" + entry.uri)
                    .then(function(response2) {
                        releases.push(response2.data);
                    }, function() {});
            });
            $scope.artist.releases = releases;
        }, function() {
            console.log("Failed to retrieve artist data");
        });
});

app.controller('labelController', function($scope, $http, $routeParams) {
    $http.get("tmp/" + $routeParams.id + ".json")
        .then(function(response) {
            $scope.label = response.data;
            console.log(response.data);
        }, function() {
            console.log("Failed to retrieve label data");
        });
});

app.controller('releaseController', function($scope, $http, $routeParams) {
    $http.get("tmp/" + $routeParams.id + ".json")
        .then(function(response) {
            $scope.release = response.data;
            console.log(response.data);
        }, function() {
            console.log("Failed to retrieve release data");
        });
});
