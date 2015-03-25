var app = angular.module("myApp", []);

app.controller("customersCtrl", function($scope, $http) {
  $http.get('/getdata/').
    success(function(data, status, headers, config) {
      $scope.posts = data;
    }).
    error(function(data, status, headers, config) {
      // log error
    });
});