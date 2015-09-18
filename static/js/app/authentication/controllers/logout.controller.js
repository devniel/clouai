/**
* LogoutController
* @namespace clouai.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.authentication.controllers')
    .controller('LogoutController', LogoutController);

  LogoutController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace LogoutController
  */
  function LogoutController($location, $scope, Authentication) {
    var vm = this;
    vm.login = login;

    activate();

    $scope.error = false;

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf clouai.authentication.controllers.LogoutController
    */
    function activate() {

      console.log('LOGOUT--------');

      debugger;
      Authentication.logout();
    }

 
  }
})();