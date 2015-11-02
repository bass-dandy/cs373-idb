var app = angular.module('meccaApp', ['ngRoute', 'ngAnimate']);

app.controller('mainController', function($scope) {
    
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

        .when('/models', {
            templateUrl : 'templates/models.html',
            controller  : 'mainController'
        })

        .when('/label/:id', {
            templateUrl : 'templates/label.html',
            controller  : 'mainController'
        })

        .when('/artist/:id', {
            templateUrl : 'templates/artist.html',
            controller  : 'mainController'
        })

        .when('/release/:id', {
            templateUrl : 'templates/release.html',
            controller  : 'mainController'
        });

    $locationProvider.html5Mode(true);
});

app.controller('artistController', function($scope, $http, $routeParams) {
    $http.get("tmp/" + $routeParams.id + ".json")
        .then(function(response) {
            $scope.artist = response.data;
            console.log(response.data);
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
