export abstract class Animal {
  /** @param {number} value The length of the animal in parrots. */
  protected constructor(public value: number) {}

  convertTo(someone: Animal): number {
    if (someone instanceof Parrot) {
      return 38;
    } else if (someone instanceof Monkey) {
      return 5;
    } else {
      this.value = 0;
      return 0;
    }
  }
}

export class Boa extends Animal {
  constructor() {
    super(1);
  }
  convertTo(someone: Animal): number {
    if (someone instanceof Parrot) {
      return 38;
    } else if (someone instanceof Monkey) {
      return 5;
    }
    return 0;
  }
}

export class Parrot extends Animal {
  constructor() {
    super(1);
  }
  convertTo(someone: Animal): number {
    if (someone instanceof Boa) {
      return 1;
    }
    if (someone instanceof Monkey) {
      return 1;
    }
    return 0;
  }
}

export class Monkey extends Animal {
  constructor() {
    super(1);
  }
  convertTo(someone: Animal): number {
    if (someone instanceof Parrot) {
      return 1;
    } else if (someone instanceof Boa) {
      return 1;
    }
    return 0;
  }
}
