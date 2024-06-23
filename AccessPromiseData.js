var promiseObj = new Promise(function (resolve, reject) {
  resolve({
    name: "sagar",
    gender: "male",
  });
});
console.log(promiseObj);
//how to access data of Promise Object
promiseObj
  .then(function (successdata) {
    console.log("then executed");
    console.log(successdata);
  })
  .catch(function (errordata) {
    console.log("catch executed");
    console.log(errordata);
  });
