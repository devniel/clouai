/**
* Property
* @namespace clouai.repository.services
*/
(function () {
  'use strict';

  angular
    .module('clouai.repository.services')
    .factory('Property', Property);

  Property.$inject = ['$cookies', '$http', 'Authentication'];

  /**
  * @namespace Repository
  * @returns {Factory}
  */
  function Property($cookies, $http) {
    
    return {
      list : function(callback){

        return $http.get('/api/v1/properties/')
        .success(function(data, status, headers, config){
          callback(null, data);
        }).error(function(data, status, headers, config){
          callback(data);
        });

      }
    };

  }

})();