/**
* Record
* @namespace clouai.repository.services
*/
(function () {
  'use strict';

  angular
    .module('clouai.repository.services')
    .factory('Record', Record);

  Record.$inject = ['$cookies', '$http', 'Authentication'];

  /**
  * @namespace Record
  * @returns {Factory}
  */
  function Record($cookies, $http, Authentication) {
    
    return {
      read : function(id, callback){

        if(Authentication.getAuthenticatedAccount().repositories.length >= 1){
          var repository = Authentication.getAuthenticatedAccount().repositories[0];

          return $http.get('/api/v1/repositories/' + repository.id + '/records/' + id + '/')
          .success(function(data, status, headers, config){
            callback(null, data);
          }).error(function(data, status, headers, config){
            callback(data);
          });
        }else{
          callback(new Error("Record with id " + id + " not found."))
        }
      },

      create : function(data, callback){
        if(Authentication.getAuthenticatedAccount().repositories.length >= 1){
          var repository = Authentication.getAuthenticatedAccount().repositories[0];

          var request = {
            method: 'POST',
            url: '/api/v1/repositories/' + repository.id + '/records/',
            data: data
          };

          return $http(request)
            .success(function(data, status, headers, config){
              callback(null, data);
            }).error(function(data, status, headers, config){
              callback(data);
            });

        }
      }
    };

  }

})();