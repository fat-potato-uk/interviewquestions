export class ItsFarTooHotError extends Error {
    constructor() {
        super("It's far too hot!");
        Object.setPrototypeOf(this, ItsFarTooHotError.prototype);
    }
}
