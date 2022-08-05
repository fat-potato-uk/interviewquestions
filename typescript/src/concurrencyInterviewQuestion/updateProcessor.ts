import { IUpdate } from "./update";

export interface IUpdateProcessor {
    process(updates: IUpdate[]): Promise<void>;
}