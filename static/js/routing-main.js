var app = angular.module('meccaApp', ['ngRoute', 'ngAnimate']);

app.controller('mainController', function($scope) {});

app.controller('artistsController', function($scope) {
    $scope.modelType = 'artists'; 
});

app.controller('labelsController', function($scope) {
    $scope.modelType = 'labels'; 
});

app.controller('releasesController', function($scope) {
    $scope.modelType = 'releases'; 
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
