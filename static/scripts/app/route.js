angular
    .module('app', ['ngRoute', 'ngCookies'])
    .config(['$routeProvider','$locationProvider',
        function($routeProvider,$locationProvider){

            $routeProvider.when('/',{
                templateUrl: 'static/templates/main.html',
                controller: 'homeController',
                controllerAs: 'vm'
            })

            .when('/login', {
                templateUrl: 'static/templates/login.html',
                controller: 'loginController',
                controllerAs: 'vm'
            })

            .when('/register', {
                templateUrl: 'static/templates/register.html',
                controller: 'registerController',
                controllerAs: 'vm'
            })

            .when('/update', {
                templateUrl: 'static/templates/update.html',
            })
        }
    ]);
