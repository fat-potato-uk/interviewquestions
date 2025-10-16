export class TemperatureConstantGetter {
    async getHotnessConstant(): Promise<number> {
        // We call an external service to get the constant, so first, build the request
        var request = new Request('https://api.nasa.gov/magicConstantValue1', {
            method: 'GET',
            headers: {
                accept: 'application/json'
            }
        });
        // Then send the request
        return await this.makeRequest(request);
    }

    async getHumidityConstant(): Promise<number> {
        // We call an external service to get the constant, so first, build the request
        var request = new Request('https://api.nasa.gov/magicConstantValue2', {
            method: 'GET',
            headers: {
                accept: 'application/json'
            }
        });
        // Then send the request
        return await this.makeRequest(request);
    }

    private async makeRequest(request: Request): Promise<number> {
        let response: Response;
        try {
            response = await fetch(request);
        } catch (error) {
            console.error(error);
            return 0;
        }
        return parseInt(await response.text());
    }
}
