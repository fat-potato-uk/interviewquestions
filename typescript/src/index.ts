import { ConcurrencyInterviewQuestions } from "./concurrencyInterviewQuestion/concurrenyInterviewQuestions";
import { IUpdate } from "./concurrencyInterviewQuestion/update";

const update1: IUpdate = {
    name: "test1",
    data: "test1",
    processed: new Date(),
    version: "234"
}

const update2: IUpdate = {
    name: "test2",
    data: "test2",
    processed: new Date(),
    version: "4"
}

const test = new ConcurrencyInterviewQuestions({ process: async (updates) => console.log(updates)});
console.log("send updates");
test.processUpdate(update1)
test.processUpdate(update2)
console.log("finish updates");