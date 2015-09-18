/**
* Register controller
* @namespace clouai.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.authentication.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    activate();

    $scope.error = false;

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf thinkster.authentication.controllers.RegisterController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
    * @name register
    * @desc Register a new user
    * @memberOf thinkster.authentication.controllers.RegisterController
    */
    function register() {
      Authentication.register(
        vm.email, 
        vm.password, 
        vm.username,
        function onSuccess(data, status, headers, config){
          console.log(status, data);
        },
        function onError(data, status, headers, config){
          console.log(data);
          var description = '';
          var errors = data.data;
          var description = [];
          for(var i in errors){
            description.push(i + ' : ' + errors[i])
          }
          $scope.error = data.message + " <br/> " + description.join('<br/>');
        }
      );
    }
  }
})();