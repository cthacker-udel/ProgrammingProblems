Object.defineProperty( Array.prototype, "foldr", { value: function foldr(fn,z) {
    return function _foldr(a) {
        if (a.length > 0) {
            value_ =  fn(a[0], z);
            if (value_ === 
            return fn(a[0], _foldr(a.slice(1)));
        }
        return z;
    } (this)
  } } );
  
  Object.defineProperty( String.prototype, "foldr", { value: [].foldr } );


const nil = (x, z) => false;
let i = 0;
const arg = [1, 2, 3];
const logging = fn => function logging(...a) { i++; return fn(...a); } ;
console.log(arg.foldr(logging(nil), true));
console.log(i);
