Array.prototype.sameStructureAs = function (other) {
  /**
   *
   * @param {any[]} arr
   */
  const mapStructure = (
    arr,
    mappedDepth = { 0: { 0: 0 } },
    elemNumber = 0,
    currentLevel = 0
  ) => {
    for (let i = 0; i < arr.length; i++) {
      const eachelement = arr[i];
      if (eachelement.constructor.name === "Array") {
        mapStructure(eachelement, mappedDepth, i, currentLevel + 1);
      } else if (elemNumber in mappedDepth) {
        if (currentLevel in mappedDepth[elemNumber]) {
          mappedDepth[elemNumber][currentLevel] += 1;
        } else {
          mappedDepth[elemNumber][currentLevel] = 1;
        }
      } else {
        mappedDepth[elemNumber] = {};
        mappedDepth[elemNumber][currentLevel] = 1;
      }
    }
    return mappedDepth;
  };
  if (
    typeof other !== "object" ||
    typeof this !== "object" ||
    other.constructor.name !== "Array" ||
    this.constructor.name !== "Array"
  ) {
    return false;
  }
  const mapStructureOther = mapStructure(other);
  const mapStructureThis = mapStructure(this);
  return JSON.stringify(mapStructureOther) === JSON.stringify(mapStructureThis);
};

console.log([1, 1, 1].sameStructureAs([2, 2, 2]), "[1,1,1] same as [2,2,2]");

console.log(
  [1, [1, 1]].sameStructureAs([2, [2, 2]]) === true
  //   "[1,[1,1]] same as [2,[2,2]]"
);
console.log(
  [(1, [1, 1])].sameStructureAs([[2, 2], 2]) === false
  //   "[1,[1,1]] not same as [[2,2],2]"
);
console.log(
  [1, [1, 1]].sameStructureAs([2, [2]]) === false
  //   "[1,[1,1]] not same as [2,[2]]"
);

console.log(
  [[[], []]].sameStructureAs([[[], []]]) === true
  //   "[[[],[]]] same as [[[],[]]]"
);
console.log(
  [[[], []]].sameStructureAs([[1, 1]]) === false
  //   "[[[],[]]] not same as [[1,1]]"
);

console.log([1, [[[1]]]].sameStructureAs([2, [[[2]]]]) === true);
// , "[1,[[[1]]]] same as [2,[[[2]]]]");

console.log([].sameStructureAs(1) === false);
// , "[] not same as 1");
console.log([].sameStructureAs({}) === false);
// , "[] not same as {}");

console.log(
  [1, "[", "]"].sameStructureAs(["[", "]", 1]) === true
  //   "[1,'[',']'] same as ['[',']',1]"
);

console.log([1, 2].sameStructureAs([[3], 3]) === false);
// , "[1,2] not same as [[3],3]");
