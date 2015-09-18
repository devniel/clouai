/**
* DashboardController
* @namespace clouai.layout.controllers
*/
(function () {
  'use strict';

  angular
    .module('clouai.layout.controllers')
    .controller('DashboardController', DashboardController);

  DashboardController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace NavbarController
  */
  function DashboardController($scope, Authentication) {
    var vm = this;
  }
  
})();