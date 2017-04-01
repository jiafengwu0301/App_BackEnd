angular
    .module('app', ['ngRoute'])
    .config(['$routeProvider','$locationProvider',
        function($routeProvider,$locationProvider){

            $routeProvider.when('/',{
                templateUrl: 'static/templates/main.html',
                // controller: 'homeController',
                // controllerAs: 'vm'
            })

            .when('/login', {
                templateUrl: 'static/templates/login.html',
            })

            .when('/register', {
                templateUrl: 'static/templates/register.html',
            })

            .when('/update', {
                templateUrl: 'static/templates/update.html',
            })
        }
    ]);
