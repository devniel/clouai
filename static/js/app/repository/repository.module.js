(function () {
  'use strict';

  angular
    .module('clouai.repository', [
      'clouai.repository.controllers',
      'clouai.repository.services',
      'clouai.repository.directives',
      'ngSanitize'
    ]);

  angular
    .module('clouai.repository.controllers', []);

  angular
    .module('clouai.repository.services', ['ngCookies']);

  angular
    .module('clouai.repository.directives', []);

})();