/**
* DashboardController
* @namespace clouai.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.layout.controllers')
    .controller('LandingController', LandingController);

  LandingController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function LandingController($scope, Authentication) {
    var vm = this;
  }
  
})();