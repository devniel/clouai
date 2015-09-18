/**
* RecordsController
* @namespace clouai.repository.controllers
*/
(function () {
  'use strict';

  angular
  .module('clouai.repository.controllers')
  .controller('RecordsFormController', ["$location", "$scope", "Repository", "Property", "Record",
  function ($location, $scope, Repository, Property, Record) {

    var self = this;

    // Data
    this.properties = [];
    this.record = {};

    // Getting properties
    Property.list(function(err, data){
      if(err) return console.error(err);
      self.properties = data;
    });

    // Add properties
    this.addProperty = function(id){      
      for(var i in self.properties){
        if(self.properties[i].id == id){
          var new_property = angular.copy(self.properties[i]);
          delete new_property.value;

          if(i < self.properties.length - 1){
            self.properties.splice(parseInt(i)+1, 0, new_property);
          }else{
            self.properties.push(new_property);
          }
          break;
        }
      }
    }

    // Submit form
    this.submit = function(){      
      Record.create(self.properties, function(err, data){
        if(err) throw err;
        window.location = '/';
      })
    }



  }]);

})();