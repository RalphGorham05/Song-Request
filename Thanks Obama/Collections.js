
var db = new MongoInternals.RemoteCollectionDriver('mongodb://localhost:27017/test');



Items = new Mongo.Collection("JobExplorer", {_driver: db });
Surveys = new Mongo.Collection("PersonalSurvey", {_driver: db});
Employers = new Mongo.Collection("EmployerSurvey", {_driver: db});	