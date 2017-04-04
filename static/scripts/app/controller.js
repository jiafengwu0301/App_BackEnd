angular
    .module('app')
    .controller('homeController', homeController)
    .controller('loginController', loginController)
    .controller('registerController', registerController)
    .controller('updateController', updateController)

function homeController($route, $location,$rootScope,$facebook){
    var vm = this;

    vm.currentAccount = $rootScope.globals.currentAccount.account;
    vm.isLoggedIn = false;
    vm.facebook = facebook;
    vm.welcomeMsg = null;

    function facebook(){
        $facebook.login().then(function(){
            refresh();
        });
    }

    function refresh() {
        $facebook.api("/me").then(
            function(response) {
                vm.welcomeMsg = "Welcome " + response.name;
                vm.isLoggedIn = true;
            },
            function(err) {
                vm.welcomeMsg = "Please log in";
            });
    }

    refresh();
}

function loginController($route,$location,authenticationService){
    var vm = this;
    vm.login = login;

    (function initController() {
        authenticationService.clearCredentials();
    })();

    function login(){
        vm.dataLoading = true;
        authenticationService.login(vm.username, vm.password)
            .then(function(response){
                if (response.status == 200){
                    authenticationService.setCredentials(vm.username, vm.password, response.data.account);
                    $location.path('/');
                } else {
                    alert(response.response.data.non_field_errors);
                    vm.dataLoading=false;
                }
            })
    }
}

function registerController($q,$route,$location,$http){
    var vm = this;

    vm.register = register;

    function register(){

        vm.dataLoading = true;
        var deferred = $q.defer();

        $http.post('/accounts/create/', vm.account);

        $location.path('/#/login');

    }
}

function updateController($q,$route,$location,$http,$rootScope){
    var vm = this;

    vm.updateInfo = updateInfo;
    vm.currentAccount = $rootScope.globals.currentAccount.account;

    function updateInfo(){
        var deferred = $q.defer();
        alert(JSON.stringify(vm.update));
        $http.put('/accounts/'+vm.currentAccount.id+'/update/',vm.update);
        alert('Account Informations Changes. Require log out to complete.')
        $location.path('/#/login');
    }
}
