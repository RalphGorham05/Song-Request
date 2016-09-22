//console.log(Items.find().count());

Meteor.methods({
	'getPersonalSurvey': function(value){
		//var id = new Meteor.Collection.ObjectID("56bf8474e7ebfe1d2cb334fe");
		var id = new Meteor.Collection.ObjectID(value);
		var pes = Surveys.findOne(id);//({_id: ObjectId("56bf8474e7ebfe1d2cb334fe")})//Surveys.findOne(id);
		//console.log(pes.worklife_self);
		var returnType = { worklife: 0, jobsec: 0,
td: 0, workload: 0, careerpath: 0, promocrit: 0,
promo: 0, auton: 0, salary: 0, goodsup: 0,
flex: 0, rewperf: 0, mission: 0, health: 0,
rewrecog: 0, workspace: 0, poorperfs: 0};

		returnType.worklife = pes.worklife_self;
		returnType.jobsec = pes.jobsec_self;
		returnType.td = pes.td_self;
		returnType.workload = pes.workload_self;
		returnType.careerpath = pes.careerpath_self;
		returnType.promocrit = pes.promocrit_self;
		returnType.promo = pes.promo_self;
		returnType.auton = pes.auton_self;
		returnType.salary = pes.salary_self;
		returnType.goodsup = pes.goodsup_self;
		returnType.flex = pes.flex_self;
		returnType.rewperf = pes.rewperf_self;
		returnType.mission = pes.mission_self;
		returnType.health = pes.health_self;
		returnType.rewrecog = pes.rewrecog_self;
		returnType.workspace = pes.workspace_self;
		returnType.poorperfs = pes.poorperfs_self;
		for (var key in returnType) {
    	// skip loop if the property is from prototype
    		if (!returnType.hasOwnProperty(key)) continue;
    		returnType[key] *= 20;
    		
		}
		//console.log(returnType.jobsec);
		
		return returnType;
	},
	/*
	'findMismatch' : function(user, emps){
		var allMatches = [];
		for(var i = 0; i < emps.length; i++){
			//var temp = emps[i];
			allMatches.push(getRank(user,emps[i]);
		}

	}
	*/

	'getEmployers' : function(){
		var emps = Employers.find().fetch();
		//var emps = Employers.find( distinct: "cur_emp_name" );
		return emps;
	},

	'getRank' : function(user, emp){
		var rank = {emp: null, rank: 0.0};

		
		if (user.length != emp.length){
			return 0;
		}
		var matchAvg = 0;

		matchAvg += Math.abs(user.worklife - emp.worklife);
		matchAvg += Math.abs(user.jobsec - emp.jobsec);
		matchAvg += Math.abs(user.td - emp.td);
		matchAvg += Math.abs(user.workload - emp.workload);
		matchAvg += Math.abs(user.careerpath - emp.careerpath);
		matchAvg += Math.abs(user.promocrit - emp.promocrit);
		matchAvg += Math.abs(user.promo - emp.promo);
		matchAvg += Math.abs(user.auton - emp.auton);
		matchAvg += Math.abs(user.salary - emp.salary);
		matchAvg += Math.abs(user.goodsup - emp.goodsup);
		matchAvg += Math.abs(user.flex - emp.flex);
		matchAvg += Math.abs(user.rewperf - emp.rewperf);
		matchAvg += Math.abs(user.mission - emp.mission);
		matchAvg += Math.abs(user.health - emp.health);
		matchAvg += Math.abs(user.rewrecog - emp.rewrecog);
		matchAvg += Math.abs(user.workspace - emp.workspace);
		matchAvg += Math.abs(user.poorperfs - emp.poorperfs);
		
		matchAvg = matchAvg / 17;
		rank.emp = emp;
		rank.rank = matchAvg;
		return rank;

	},
	'lastPersonalSurvey' :function(value){
		var id = new Meteor.Collection.ObjectID(value);
		var je = Items.findOne(id);
		var len = je.personalSurveys.length;
		if(len < 1)
			return null;
		id = new Meteor.Collection.ObjectID(je.personalSurveys[len-1]._str);
		var ps = Surveys.findOne(id);
		return ps;

	},
	'checkSurveyDate' : function(value, num){
		var id = new Meteor.Collection.ObjectID(value);
		var surv;
		//Personal Survey
		if(num == 0){
			surv = Surveys.findOne(id);
			//console.log(surv.timeStamp);
		}
		//Employer
		else if(num == 1){
			surv = Employers.findOne(id);
		}else {return false;}
		if(surv == null)
			return false;
		var date = new Date(surv.timeStamp);
		var newdate = new Date(new Date(surv.timeStamp).setMonth(date.getMonth() + 6));
		if(new Date() > newdate)
			return true;
		return false;

	},
	'sumEmployers' : function(){
		var as = Employers.find({}).fetch();
		var emps = [];
		if(as == null)
			return emps;		
    	var temp = { name : as[0].cur_emp_name, count: 1
    				, jobsec: as[0].jobsec_cur, worklife: as[0].worklife_cur, workload: as[0].workload_cur
    				,careerpath: as[0].careerpath_cur, td: as[0].td_cur,   promocrit: as[0].promocrit_cur,
promo: as[0].promo_cur, auton: as[0].auton_cur, salary: as[0].salary_cur, goodsup: as[0].goodsup_cur,
flex: as[0].flex_cur, rewperf: as[0].rewperf_cur, mission: as[0].mission_cur, health: as[0].health_cur,
rewrecog: as[0].rewrecog_cur, workspace: as[0].workspace_cur, poorperfs: as[0].poorperfs_cur};
		emps.push(temp);
    	var k = 0;
    	var ent;
    	
		for (var key in as) {
			k++;
			if(k == 1){
				continue;
			}
			ent = false;
    	// skip loop if the property is from prototype
    		if (!as.hasOwnProperty(key)) continue;
    		for(var i = 0; i < emps.length; i++){
    			if(emps[i].name == as[key].cur_emp_name){

    				emps[i].count++;
    				var ct = emps[i].count;
    				var oct = emps[i].count - 1;
    				emps[i].jobsec = ((oct * emps[i].jobsec) + as[key].jobsec_cur)/ct;
    				emps[i].worklife = ((oct * emps[i].worklife) + as[key].worklife_cur)/ct;
    				emps[i].workload = ((oct * emps[i].workload) + as[key].workload_cur)/ct;
    				emps[i].careerpath = ((oct * emps[i].careerpath) + as[key].careerpath_cur)/ct;
    				emps[i].td = (oct * emps[i].td) + as[key].td_cur;
    				emps[i].td /= ct;
    				emps[i].promocrit = (oct * emps[i].promocrit) + as[key].promocrit_cur;
    				emps[i].promocrit /= ct;
					emps[i].promo = (oct * emps[i].promo) + as[key].promo_cur; 
					emps[i].promo /= ct;
					emps[i].auton = (oct * emps[i].auton ) + as[key].auton_cur;
					emps[i].auton /= ct;
					emps[i].salary = (oct * emps[i].salary) + as[key].salary_cur;
					emps[i].salary /= ct;
					emps[i].goodsup = (oct * emps[i].goodsup) + as[key].goodsup_cur;
					emps[i].goodsup /= ct;
					emps[i].flex = (oct * emps[i].flex) + as[key].flex_cur;
					emps[i].flex /= ct;
					emps[i].rewperf = (emps[i].rewperf * oct) + as[key].rewperf_cur;
					emps[i].rewperf /= ct;
					emps[i].mission = (emps[i].mission * oct ) + as[key].mission_cur;
					emps[i].mission /= ct;
					emps[i].health = (emps[i].health * oct) + as[key].health_cur;
					emps[i].health /= ct;
					emps[i].rewrecog = (emps[i].rewrecog * oct) + as[key].rewrecog_cur;
					emps[i].rewrecog /=ct;
					emps[i].workspace = (oct * emps[i].workspace) + as[key].workspace_cur;
					emps[i].workspace /= ct;
					emps[i].poorperfs = (oct * emps[i].workspace) +  as[key].poorperfs_cur;
					emps[i].poorperfs /= ct;

					/*for(var j = 2; j < emps[i].length; j++){
						emps[i][j] /= emps[i].count;
					}*/
					ent = true;
					break;
    			}
    			
    			
    		}
    		if(ent == false){
    			var x;
    			x = { name : as[key].cur_emp_name, count: 1
    				, jobsec: as[key].jobsec_cur, worklife: as[key].worklife_cur, workload: as[key].workload_cur
    				,careerpath: as[key].careerpath_cur, td: as[key].td_cur,   promocrit: as[key].promocrit_cur,
promo: as[key].promo_cur, auton: as[key].auton_cur, salary: as[key].salary_cur, goodsup: as[key].goodsup_cur,
flex: as[key].flex_cur, rewperf: as[key].rewperf_cur, mission: as[key].mission_cur, health: as[key].health_cur,
rewrecog: as[key].rewrecog_cur, workspace: as[key].workspace_cur, poorperfs: as[key].poorperfs_cur};
    			emps.push(x);
    		}
    		
    			
    		
		}
		
		
		return emps;
	}


});
/*
//Matching Algorithm
var userinfo;
var businesses;
Meteor.call('getPersonalSurvey', "56bf8474e7ebfe1d2cb334fe", function(error, result){
	if(error){
		console.log(error);
	}else{
		console.log("I have a result");
		for (var key in result) {
    	// skip loop if the property is from prototype
    		if (!result.hasOwnProperty(key)) continue;
    		var obj = result[key];
    		//console.log(obj);
    		
		}
		userinfo = result;
	}
});


Meteor.call('sumEmployers', function(error, result){
	if(error)
		console.log(error);
	else
		businesses = result;

});
//console.log(businesses);
var last_list = [];
for(var i = 0; i < businesses.length; i++){
	Meteor.call('getRank', userinfo, businesses[i], function(error, result){
		if(error)
			console.log(error);
		else{
			last_list.push(result);
		}

	});
}
last_list.sort(function(a,b){return a.rank - b.rank});
console.log(last_list);
*/


/*
Meteor.call('checkSurveyDate', "56bf8474e7ebfe1d2cb334fe", 0, function(error, result){
	if(error)
		console.log(error);
	else
		console.log(result);

});



Meteor.call('lastPersonalSurvey', "56bf8474e7ebfe1d2cb33500", function(error, result){
	if(error)
		console.log(error);
	else{
		
		var date = new Date(result.timeStamp);
		var newdate = new Date(new Date(result.timeStamp).setMonth(date.getMonth() + 6));
		console.log(newdate);
		console.log(new Date());
		if(new Date() > newdate){
			console.log("Change it");
		}
	}
		
});
//Retrieve Employers


var user_rating;
var emps;
Meteor.call('getPersonalSurvey', "56bf8474e7ebfe1d2cb334fe", function(error, result){
	if(error){
		console.log(error);
	}else{
		//console.log("I have a result");
		user_rating = result;
	}
});



Meteor.call('getEmployers', function(error, result){
	if(error){
		console.log("first error")
		console.log(error);
	}
	else{
		Meteor.call('getRank',user_rating, result[0],  function(err, res){
			if(err){ 
				console.log("sec error");
				console.log(err);
		}
		
			else{
				console.log("I have an answer");
				console.log(res.rank);
				console.log(res.emp.cur_emp_name)
			}
		});
	
	}
		
});

*/
/*function(error, result)){
	if(error){
		console.log(error);
	}else{
		console.log("I have a value");
	}


});


Meteor.call('getPersonalSurvey', "56bf8474e7ebfe1d2cb334fe", function(error, result){
	if(error){
		console.log(error);
	}else{
		console.log("I have a result");
		for (var key in result) {
    	// skip loop if the property is from prototype
    		if (!result.hasOwnProperty(key)) continue;
    		var obj = result[key];
    		console.log(obj);
    		
		}
	}
});*/