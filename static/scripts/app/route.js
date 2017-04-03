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
                controller: 'updateController',
                controllerAs: 'vm'
            })
        }
    ])
    .run(run);

run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
function run($rootScope, $location, $cookies, $http) {
    // keep user logged in after page refresh
    $rootScope.globals = $cookies.getObject('globals') || {};
    if ($rootScope.globals.currentAccount) {
        $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentAccount.authdata; // jshint ignore:line
    }

    $rootScope.$on('$locationChangeStart', function (event, next, current) {
        // redirect to login page if not logged in and trying to access a restricted page
        var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
        var loggedIn = $rootScope.globals.currentAccount;
        if (restrictedPage && !loggedIn) {
            $location.path('/login');
        }
    });
}
