/**
 * Record
 * @namespace clouai.repository.directives
 */
(function () {
  'use strict';

  angular
    .module('clouai.repository.directives')
    .directive('record', record);

  /**
   * @namespace Record
   */
  function record() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf clouai.repository.directives.Record
     */
    var directive = {
      restrict: 'E',
      scope: {
        record: '='
      },
      templateUrl: '/static/html/repository/directives/record.html',
      link : function(scope, element) {
        // get first title
        for(var i in scope.record.properties){
          if(scope.record.properties[i].name){
            if(scope.record.properties[i].name == 'title'){
              scope.record.title = scope.record.properties[i].value;
              break;
            }
          }
        }

        if(!scope.record.title) scope.record.title = 'Untitled';
      }
    };

    return directive;
  }
})();