/**
* RecordsController
* @namespace clouai.repository.controllers
*/
(function () {
  'use strict';

  angular
  .module('clouai.repository.controllers')
  .controller('RecordsController', ["$location", "$scope", "Repository","Property",
  function ($location, $scope, Repository, Property) {

    // Data
    $scope.records = [];
    $scope.properties = [];
    $scope.record = {};
    $scope.repository = {}

    // Switchers
    $scope.no_records = true;

    // Getting records
    Repository.getRepository(function(err, data){
    	if(err) return console.error(err);

  		$scope.repository = data;      
  		
  		if($scope.repository != null){
  	  		$scope.records = $scope.repository.records;
          if($scope.records.length > 0)
            $scope.no_records = false;
  		}
    });

    // Getting properties
    Property.list(function(err, data){
      if(err) return console.error(err);
      console.log("AVAILABLE PROPERTIES ====> ", data);
      $scope.properties = data;
    });

    // Add properties
    $scope.addProperty = function(id){

      console.log("ADD PROPERTY ================== : ", id);
      
      for(var i in $scope.records){
        if($scope.records[i].id == id){
          $scope.records.splice(i, 0, $scope.records[i]);
          break;
        }
      }
    }



  }]);

})();