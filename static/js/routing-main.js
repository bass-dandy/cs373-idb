var app = angular
    .module('meccaApp', ['ngRoute', 'ngAnimate', 'ngSanitize'])
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

app.controller('mainController', function() {});

app.controller('navbarController', function($scope, $location, Sources) {
    $scope.query = "";
    $scope.prefetch = {
        artists:  [],
        labels:   [],
        releases: []
    };

    $scope.search = function(q) {
        $location.path('/search/' + q);
    }

    $scope.blur = function() {
        setTimeout(function() {
            $scope.focus = false;
            $scope.$apply();
        }, 100);
    };

    $scope.$watch('query', function() {
        if($scope.query.length > 3) {
            Sources.fromUri("/api/?q=" + $scope.query)
                .then(function(res) {
                    $scope.prefetch = res.data;
                }, function() {});
        } else {
            $scope.prefetch = {
                artists:  [],
                labels:   [],
                releases: []
            };
        }
    });
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

app.controller('modelsController', function($scope, $http) {
    $scope.order = "asc";
    $scope.currentPage = 1;
    $scope.models = [];
    $scope.prev   = [];
    $scope.next   = [];

    var getModels = function() {
        $http.get("http://downing.club/api/" + $scope.modelType + "?pagesize=12&page=" + $scope.currentPage + "&order=" + $scope.order)
            .then(function(res) {
                if($scope.modelType == 'labels') {
                    res.data.forEach(function(entry) {
                        entry.medium_image = entry.small_image;
                    });
                }
                $scope.models = res.data;
            });
    };
    getModels();
    
    $scope.setOrder = function(order) {
        if(order != $scope.order) {
            $scope.order = order;
            $scope.currentPage = 1;
            getModels();
        }
    }
    $scope.goToPrev = function() {
        $scope.currentPage--;
        getModels();
    };
    $scope.goToNext = function() {
        $scope.currentPage++;
        getModels();
    };
});

app.controller('artistsController', function($scope) {
    $scope.modelType = 'artists'; 
});

app.controller('labelsController', function($scope) {
    $scope.modelType = 'labels'; 
});

app.controller('releasesController', function($scope) {
    $scope.modelType = 'releases'; 
});

app.controller('searchController', function($scope, $routeParams, Sources) {
    Sources.fromUri("/api/?q=" + $routeParams.id)
        .then(function(response) {
            $scope.results = response.data;
        }, function() {});
});

app.controller('pokemastersController', function($scope, $http) {
    $scope.setIdx = function(idx) {
        $scope.pokemonIdx = idx;
    }
    $http.get("tmp/pokemon.json")
        .then(function(res) {
            $scope.pokemen = res.data.pokemon;
        }, function() {});
});

app.config(function($routeProvider, $locationProvider, $animateProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'templates/splash.html',
            controller  : 'mainController'
        })

        .when('/pokemasters', {
            templateUrl : 'templates/pokemasters.html',
            controller  : 'pokemastersController'
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
        })

        .when('/search/:id', {
            templateUrl : 'templates/search.html',
            controller  : 'searchController'
        });

    $locationProvider.html5Mode(true);
    $animateProvider.classNameFilter(/^(?:(?!ng-animate-disabled).)*$/);
});

app.controller('artistController', function($scope, $routeParams, $http, Sources) {
    // For selecting a random album cover
    $scope.artIdx = 0;

    // For making hashtags linkable
    $scope.parseHashtags = function(input) {
        return input.replace(/(^|\W)(#[a-z\d][\w-]*)/ig, function(match) {
            match = match.trim().substr(1);
            return "<a href='https://twitter.com/hashtag/" + match + "'>#" + match + "</a> ";
        });
    };

    // Get artist data
    Sources.fromUri("/api/artists/" + $routeParams.id)
        .then(function(response) {
            $scope.artist = response.data;
            $scope.artIdx = Math.floor(Math.random() * response.data.releases.length);

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

            // Parse discussion
            $scope.artist.discussion.forEach(function(entry) {
                entry.discussion = parseHashtags(entry.discussion);
            });
        }, function() {});

    // For posting comments and replies
    var req = {
        method: 'POST',
        url: '',
        headers: {
            'Content-Type': 'application/json'
        },
        data: ''
    };

    $scope.postComment = function() {
        req.url = "http://downing.club/api/artists/" + $scope.artist.id + "/discussions";
        req.data = { 'discussion': $scope.submission };
        $http(req).then(function(res) { 
            Sources.fromUri("/api/artists/" + $scope.artist.id)
                .then(function(response) {
                    $scope.artist.discussion = response.data.discussion;
                    $scope.submission = "";
                }, function() {});
        }, function() {});
    };

    $scope.postReply = function(body, id) {
        if(body.length > 0) {
            req.url = "http://downing.club/api/discussions/" + id;
            req.data = { 'reply': body };
            $http(req).then(function(res) { 
                Sources.fromUri("/api/artists/" + $scope.artist.id)
                    .then(function(response) {
                        $scope.artist.discussion = response.data.discussion;
                    }, function() {});
            }, function() {});
        }
    };
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
    // Fetch data
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

    // Set up audio playback
    $scope.audio = new Audio();

    // Playback controls
    $scope.togglePlayback = function(url) {
        if($scope.audio.src != url) {
            $scope.audio.src = url;
            $scope.audio.play();
        } else if($scope.audio.paused) {
            $scope.audio.play();
        } else {
            $scope.audio.pause();
        }
    };
    // For hiding/showing playback buttons
    $scope.showPause = function(src) {
        return $scope.audio.src == src && !$scope.audio.paused && !$scope.audio.ended;
    };
    // Stop audio when leaving the page
    $scope.$on('$destroy', function() {
        $scope.audio.pause();
    });
});
