/**
* LoginController
* @namespace clouai.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.authentication.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace LoginController
  */
  function LoginController($location, $scope, Authentication) {
    var vm = this;
    vm.login = login;

    activate();

    $scope.error = false;

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf clouai.authentication.controllers.LoginController
    */
    function activate() {
      // If the user is authenticated, they should not be here.
      Authentication.unauthenticate();
    }

    /**
    * @name login
    * @desc Log the user in
    * @memberOf clouai.authentication.controllers.LoginController
    */
    function login() {
      Authentication.login(
        vm.email, 
        vm.password, 
        function onSuccess(){},
        function onError(data, status, headers, config){
          $scope.error = 'Incorrect username or password';
        });
    }
  }
})();