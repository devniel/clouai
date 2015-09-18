(function () {
	'use strict';

	angular
	.module('clouai', [
	  'clouai.config',
	  'clouai.routes',
	  'clouai.authentication',
	  'clouai.layout'
	]);

	angular
	.module('clouai.routes', ['ngRoute']);

	angular
		.module('clouai.config', []);

	angular
	.module('clouai')
	.run(run);

	run.$inject = ['$http'];

	/**
	* @name run
	* @desc Update xsrf $http headers to align with Django's defaults
	*/
	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	}


})();