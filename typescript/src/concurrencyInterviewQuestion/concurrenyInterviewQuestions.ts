import { IUpdate } from './update';
import { IUpdateProcessor } from './updateProcessor';

export class ConcurrencyInterviewQuestions {
    // An array that stores the most current updates
    private readonly currentUpdates: IUpdate[] = [];

    // Promise used to track if a call to the update processor has been scheduled
    private batchUpdatePromise: Promise<void> | null = null;

    constructor(private readonly updateProcessor: IUpdateProcessor) {}

    /**
     * This function is called by a HTTP POST request handled in another class. Prevents downstream system
     * from receiving multiple updates one after another (by only sending one at max every 5 seconds).
     */
    public processUpdate(update: IUpdate): void {
        this.currentUpdates.push(update);

        // If there is no scheduled task for the future, create one, otherwise finish
        if (this.batchUpdatePromise == null) {
            this.batchUpdatePromise = this.scheduleUpdate();
        }
    }

    private async scheduleUpdate(): Promise<void> {
        // Waits for for 5 seconds
        await new Promise((f) => setTimeout(f, 5000));
        await this.doUpdate();
    }

    private async doUpdate(): Promise<void> {
        await this.updateProcessor.process(this.currentUpdates);
        this.currentUpdates.length = 0;
        this.batchUpdatePromise = null;
    }
}
