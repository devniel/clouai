(function () {
  'use strict';

  angular
    .module('clouai.authentication', [
      'clouai.authentication.controllers',
      'clouai.authentication.services',
      'ngSanitize'
    ]);

  angular
    .module('clouai.authentication.controllers', []);

  angular
    .module('clouai.authentication.services', ['ngCookies']);
})();