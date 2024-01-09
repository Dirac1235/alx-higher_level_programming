#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    list.forEach(element => {
      if (element === searchElement)  {
        count += 1;
      }
    });
    return count;
}
