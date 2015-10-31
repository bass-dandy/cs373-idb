var app = angular.module('meccaApp', ['ngRoute']);

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
