var app = angular.module("myApp", []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});

app.controller("customersCtrl", function($scope, $http) {
  $http.get('/getdata/').
    success(function(data, status, headers, config) {
      $scope.posts = data;
      console.log($scope.posts);
    }).
    error(function(data, status, headers, config) {
      // log error
    });
});