/**
* Repository
* @namespace clouai.repository.services
*/
(function () {
  'use strict';

  angular
    .module('clouai.repository.services')
    .factory('Repository', Repository);

  Repository.$inject = ['$cookies', '$http', 'Authentication'];

  /**
  * @namespace Repository
  * @returns {Factory}
  */
  function Repository($cookies, $http, Authentication) {
    
    return {
      getRepository : function(callback){

        console.log(Authentication.getAuthenticatedAccount());

        if(Authentication.getAuthenticatedAccount() == undefined)
          Authentication.logout()

        if(Authentication.getAuthenticatedAccount().repositories.length >= 1){
            var repository = Authentication.getAuthenticatedAccount().repositories[0];
            return $http.get('/api/v1/repositories/' + repository.id + '/')
            .success(function(data, status, headers, config){
              callback(null, data);
            }).error(function(data, status, headers, config){
              callback(data);
            });
        }else{
          callback(new Error("No repositories available"))
        }
      }
    };

  }

})();