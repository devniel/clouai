/**
* NavbarController
* @namespace clouai.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function NavbarController($scope, Authentication) {
    
    var vm = this;
    vm.logout = logout;

    $scope.active = '/';

    /**
    * @name logout
    * @desc Log the user out
    * @memberOf thinkster.layout.controllers.NavbarController
    */
    function logout() {
      Authentication.logout();
    }

    $scope.$on('$routeChangeStart',function (event, next, current){
        $scope.active = next.originalPath;
    });


  }
})();