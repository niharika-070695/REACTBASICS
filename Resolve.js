//How to add or store data in the Promise object using resolve()

var promiseObj = new Promise(function (resolve, reject) {
  resolve({
    name: "sagar",
    gender: "male",
  });
});
console.log(promiseObj);
