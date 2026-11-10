import asyncio
import aiohttp

API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleVariableList?format=json"


async def fetch_car_data():
    print("Loading vehicle data...")
    try:
        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(API_URL) as response:
                response.raise_for_status()
                data = await response.json()

        filtered_data = [
            item for item in data.get("Results", [])
            if item.get("GroupName") == "Active Safety System"
        ]
        print("\nACTIVE SAFETY SYSTEM VEHICLE DATA")
        print("-" * 50)
        if not filtered_data:
            print("No matching items were found.")
        else:
            for item in filtered_data:
                print(f"ID: {item.get('ID')}")
                print(f"Name: {item.get('Name')}")
                print(f"Group: {item.get('GroupName')}")
                print("-" * 50)
        print(f"\nTotal matching items: {len(filtered_data)}")
    except aiohttp.ClientError as error:
        print(f"API request failed: {error}")
    except asyncio.TimeoutError:
        print("Error: The request timed out.")
    except ValueError:
        print("Error: Could not process the JSON response.")


if __name__ == "__main__":
    asyncio.run(fetch_car_data())
