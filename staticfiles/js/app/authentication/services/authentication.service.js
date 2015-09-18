/**
* Authentication
* @namespace clouai.authentication.services
*/
(function () {
  'use strict';

  angular
    .module('clouai.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
  * @namespace Authentication
  * @returns {Factory}
  */
  function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
    var Authentication = {
      getAuthenticatedAccount: getAuthenticatedAccount,
      isAuthenticated: isAuthenticated,
      login: login,
      register: register,
      setAuthenticatedAccount: setAuthenticatedAccount,
      unauthenticate: unauthenticate,
      logout: logout
    };

    return Authentication;

    ////////////////////

    /**
    * @name register
    * @desc Try to register a new user
    * @param {string} username The username entered by the user
    * @param {string} password The password entered by the user
    * @param {string} email The email entered by the user
    * @returns {Promise}
    * @memberOf thinkster.authentication.services.Authentication
    */
    function register(email, password, username, onSuccess, onError) {
      return $http.post('/api/v1/users/', {
        username: username,
        password: password,
        email: email
      })
      .success(function(data, status, headers, config){
        Authentication.login(email, password);
      })
      .error(onError);
    }

    /**
     * @name login
     * @desc Try to log in with email `email` and password `password`
     * @param {string} email The email entered by the user
     * @param {string} password The password entered by the user
     * @returns {Promise}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function login(email, password, onSuccess, onError) {
      return $http.post('/api/v1/auth/login/', {
        email: email, password: password
      })
      .success(function(data, status, headers, config) {
        Authentication.setAuthenticatedAccount(data.data);
        window.location = '/';
      })
      .error(onError);
    }

    /**
     * @name logout
     * @desc Try to log the user out
     * @returns {Promise}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function logout() {
      return $http.post('/api/v1/auth/logout/')
        .then(logoutSuccessFn, logoutErrorFn);

      /**
       * @name logoutSuccessFn
       * @desc Unauthenticate and redirect to index with page reload
       */
      function logoutSuccessFn(data, status, headers, config) {
        Authentication.unauthenticate();

        window.location = '/';
      }

      /**
       * @name logoutErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function logoutErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }

    /**
     * @name getAuthenticatedAccount
     * @desc Return the currently authenticated account
     * @returns {object|undefined} Account if authenticated, else `undefined`
     * @memberOf thinkster.authentication.services.Authentication
     */
    function getAuthenticatedAccount() {
      if (!$cookies.authenticatedAccount) {
        return;
      }

      return JSON.parse($cookies.authenticatedAccount);
    }

    /**
     * @name isAuthenticated
     * @desc Check if the current user is authenticated
     * @returns {boolean} True is user is authenticated, else false.
     * @memberOf thinkster.authentication.services.Authentication
     */
    function isAuthenticated() {
      return !!$cookies.authenticatedAccount;
    }

    /**
     * @name setAuthenticatedAccount
     * @desc Stringify the account object and store it in a cookie
     * @param {Object} user The account object to be stored
     * @returns {undefined}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function setAuthenticatedAccount(account) {
      $cookies.authenticatedAccount = JSON.stringify(account);
    }

    /**
     * @name unauthenticate
     * @desc Delete the cookie where the user object is stored
     * @returns {undefined}
     * @memberOf thinkster.authentication.services.Authentication
     */
    function unauthenticate() {
      delete $cookies.authenticatedAccount;
    }

  }
})();