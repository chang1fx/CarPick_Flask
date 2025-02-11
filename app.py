from flask import Flask, render_template, request

app = Flask(__name__)

# Descriptions for body types
BODY_TYPE_DESCRIPTIONS = {
    "Sedan": "A sedan is a classic car body type known for its comfort, fuel efficiency, and spacious trunk. It's ideal for daily commuting and long trips.",
    "Hatchback": "A hatchback offers a compact design with a versatile cargo area. It's great for city driving and small families.",
    "SUV": "An SUV provides a higher driving position, ample cargo space, and off-road capability. It's perfect for families and outdoor adventures.",
    "Truck": "A truck is designed for heavy-duty tasks like towing and hauling. It's ideal for work-related activities and off-roading.",
    "Coupe": "A coupe is a sporty, two-door car with a sleek design. It's best for individuals or couples who value style and performance.",
    "Wagon": "A wagon combines the comfort of a sedan with the cargo space of an SUV. It's great for families and long trips.",
    "Minivan": "A minivan offers maximum passenger and cargo space. It's perfect for large families and road trips.",
    "Crossover": "A crossover blends the features of an SUV and a sedan. It's versatile, fuel-efficient, and great for urban and suburban driving."
}

# Descriptions for fuel types
FUEL_TYPE_DESCRIPTIONS = {
    "Electric": "Electric cars are eco-friendly, quiet, and cost-effective to run. They're ideal for short to moderate trips and urban driving.",
    "Plug-In Hybrid": "Plug-in hybrids combine electric power with a gasoline engine. They offer flexibility for both short electric trips and long-distance travel.",
    "Hybrid": "Hybrids use both gasoline and electric power for improved fuel efficiency. They're great for city and highway driving.",
    "Diesel": "Diesel engines are fuel-efficient and powerful, making them ideal for long trips and towing.",
    "Gasoline": "Gasoline cars are widely available and offer a balance of performance and affordability. They're suitable for all types of driving."
}

def CarPick(answers):
    # Initialize points for body types
    sedan_points = hatchback_points = suv_points = truck_points = coupe_points = wagon_points = minivan_points = crossover_points = 0

    # Initialize points for fuel types
    gasoline_points = diesel_points = electric_points = hybrid_points = plug_in_hybrid_points = 0

    # General Purpose
    general = int(answers["general"])
    if general == 1:
        sedan_points += 1
        hatchback_points += 1
        electric_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
    elif general == 2:
        suv_points += 1
        minivan_points += 1
        wagon_points += 1
        crossover_points += 1
    elif general == 3:
        wagon_points += 1
        crossover_points += 1
        suv_points += 1
        diesel_points += 1
        hybrid_points += 1
        gasoline_points += 1
    elif general == 4:
        truck_points += 1
        suv_points += 1
        gasoline_points += 1
        diesel_points += 1

    # Passenger Space
    passenger = int(answers["passenger"])
    if passenger == 1:
        coupe_points += 1
        sedan_points += 1
        hatchback_points += 1
        truck_points += 1
    elif passenger == 2:
        hatchback_points += 1
        sedan_points += 1
        coupe_points += 1
        truck_points += 1
    elif passenger == 3:
        suv_points += 1
        wagon_points += 1
        minivan_points += 1
        crossover_points += 1
    elif passenger == 4:
        minivan_points += 1
        suv_points += 1

    # Cargo Space
    cargo = int(answers["cargo"])
    if cargo == 1:
        coupe_points += 1
        sedan_points += 1
    elif cargo == 2:
        hatchback_points += 1
        sedan_points += 1
        crossover_points += 1
        wagon_points += 1
    elif cargo == 3:
        suv_points += 1
        wagon_points += 1
        crossover_points += 1
        truck_points += 1
        minivan_points += 1
    elif cargo == 4:
        suv_points += 1
        truck_points += 1
        minivan_points += 1

    # Comfort Level During Long Travels
    travel = int(answers["travel"])
    if travel == 1:
        hatchback_points += 1
        sedan_points += 1
        coupe_points += 1
        truck_points += 1
    elif travel == 2:
        crossover_points += 1
        wagon_points += 1
    elif travel == 3:
        minivan_points += 1
        suv_points += 1

    # Driving Style
    driving = int(answers["driving"])
    if driving == 1:
        electric_points += 1
        hatchback_points += 1
        sedan_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
    elif driving == 2:
        diesel_points += 1
        sedan_points += 1
        crossover_points += 1
        wagon_points += 1
        hatchback_points += 1
        coupe_points += 1
    elif driving == 3:
        truck_points += 1
        suv_points += 1
    elif driving == 4:
        coupe_points += 1
        sedan_points += 1

    # Trip Duration
    trip = int(answers["trip"])
    if trip == 1:
        electric_points += 1
        plug_in_hybrid_points += 1
    elif trip == 2:
        hybrid_points += 1
        plug_in_hybrid_points += 1
        electric_points += 1
    elif trip == 3:
        diesel_points += 1
        gasoline_points += 1

    # Long-Distance Travel Values
    value = int(answers["value"])
    if value == 1:
        diesel_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
        electric_points += 1
        sedan_points += 1
        hatchback_points += 1
    elif value == 2:
        suv_points += 1
        minivan_points += 1
        electric_points += 1
        plug_in_hybrid_points += 1
    elif value == 3:
        sedan_points += 1
        hatchback_points += 1
        coupe_points += 1
        electric_points += 1
    elif value == 4:
        suv_points += 1
        truck_points += 1
        minivan_points += 1

    # Towing Needs
    towing = int(answers["towing"])
    if towing == 1:
        truck_points += 1
        diesel_points += 1
        suv_points += 1
    elif towing == 2:
        suv_points += 1
        wagon_points += 1
        crossover_points += 1
    elif towing == 3:
        sedan_points += 1
        hatchback_points += 1
        coupe_points += 1

    # Fuel Efficiency
    efficiency = int(answers["efficiency"])
    if efficiency == 1:
        electric_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
        sedan_points += 1
        hatchback_points += 1
    elif efficiency == 2:
        wagon_points += 1
        crossover_points += 1
        diesel_points += 1
    elif efficiency == 3:
        truck_points += 1
        gasoline_points += 1
        suv_points += 1
        minivan_points += 1
        coupe_points += 1

    # Scenario Efficiency
    scenario = int(answers["scenario"])
    if scenario == 1:
        plug_in_hybrid_points += 1
        electric_points += 1
    elif scenario == 2:
        hybrid_points += 1
        plug_in_hybrid_points += 1
        electric_points += 1
    elif scenario == 3:
        diesel_points += 1
        hybrid_points += 1
    elif scenario == 4:
        gasoline_points += 1

    # Parking and Maneuverability
    maneuverability = int(answers["maneuverability"])
    if maneuverability == 1:
        hatchback_points += 1
        sedan_points += 1
        coupe_points += 1
        electric_points += 1
    elif maneuverability == 2:
        crossover_points += 1
        wagon_points += 1
    elif maneuverability == 3:
        truck_points += 1
        minivan_points += 1
        suv_points += 1

    # Routine Maintenance
    routine = int(answers["routine"])
    if routine == 1:
        electric_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
    elif routine == 2:
        gasoline_points += 1
    elif routine == 3:
        diesel_points += 1

    # Usability When Stopped
    usability = int(answers["usability"])
    if usability == 1:
        plug_in_hybrid_points += 1
        electric_points += 1
        hybrid_points += 1
    elif usability == 2:
        gasoline_points += 1
        diesel_points += 1

    # Mobile Battery
    battery = int(answers["battery"])
    if battery == 1:
        electric_points += 1
        plug_in_hybrid_points += 1
    elif battery == 2:
        gasoline_points += 1
        diesel_points += 1
        hybrid_points += 1

    # Price
    price = int(answers["price"])
    if price == 1:
        sedan_points += 1
        hatchback_points += 1
        gasoline_points += 1
    elif price == 2:
        crossover_points += 1
        wagon_points += 1
        hybrid_points += 1
        coupe_points += 1
    elif price == 3:
        electric_points += 1
        plug_in_hybrid_points += 1
        suv_points += 1
        truck_points += 1
        minivan_points += 1

    # Safety
    safety = int(answers["safety"])
    if safety == 1:
        hatchback_points += 1
        sedan_points += 1
        gasoline_points += 1
        coupe_points += 1
    elif safety == 2:
        wagon_points += 1
        crossover_points += 1
        hybrid_points += 1
        plug_in_hybrid_points += 1
    elif safety == 3:
        suv_points += 1
        minivan_points += 1
        truck_points += 1
        electric_points += 1

    # Reliability
    reliability = int(answers["reliability"])
    if reliability == 1:
        sedan_points += 1
        hatchback_points += 1
        coupe_points += 1
        electric_points += 1
    elif reliability == 2:
        crossover_points += 1
        wagon_points += 1
        plug_in_hybrid_points += 1
        hybrid_points += 1
        gasoline_points += 1
    elif reliability == 3:
        truck_points += 1
        suv_points += 1
        minivan_points += 1
        diesel_points += 1

    # Maintenance Costs
    maintenance = int(answers["maintenance"])
    if maintenance == 1:
        sedan_points += 1
        hatchback_points += 1
        hybrid_points += 1
        gasoline_points += 1
    elif maintenance == 2:
        crossover_points += 1
        wagon_points += 1
        plug_in_hybrid_points += 1
        coupe_points += 1
    elif maintenance == 3:
        truck_points += 1
        suv_points += 1
        minivan_points += 1
        diesel_points += 1
        electric_points += 1

    # Availability and Options
    availability = int(answers["availability"])
    if availability == 1:
        sedan_points += 1
        hatchback_points += 1
        crossover_points += 1
        suv_points += 1
        truck_points += 1
        gasoline_points += 1
    elif availability == 2:
        wagon_points += 1
        minivan_points += 1
        plug_in_hybrid_points += 1
        coupe_points += 1
        hybrid_points += 1
    elif availability == 3:
        electric_points += 1
        diesel_points += 1

    # Charging Station Availability
    answer_charging_station = int(answers["answer_charging_station"])
    if answer_charging_station == 1:
        electric_points += 1
        plug_in_hybrid_points += 1
    elif answer_charging_station == 2:
        plug_in_hybrid_points += 1
    elif answer_charging_station == 3:
        gasoline_points += 1
        diesel_points += 1
        hybrid_points += 1

    # Ride Height
    height = int(answers["height"])
    if height == 1:
        crossover_points += 1
        suv_points += 1
        truck_points += 1
        minivan_points += 1
    elif height == 2:
        sedan_points += 1
        hatchback_points += 1
        coupe_points += 1
        wagon_points += 1

    # At-Home Charging
    at_home_charging = int(answers["at_home_charging"])
    if at_home_charging == 1:
        electric_points += 1
        plug_in_hybrid_points += 1
    elif at_home_charging == 2:
        gasoline_points += 1
        diesel_points += 1
        hybrid_points += 1

    # Determine the recommended body type
    body_type_points = {
        "Sedan": sedan_points,
        "Hatchback": hatchback_points,
        "SUV": suv_points,
        "Truck": truck_points,
        "Coupe": coupe_points,
        "Wagon": wagon_points,
        "Minivan": minivan_points,
        "Crossover": crossover_points
    }

    # Determine the recommended fuel type
    fuel_type_points = {
        "Electric": electric_points,
        "Plug-In Hybrid": plug_in_hybrid_points,
        "Hybrid": hybrid_points,
        "Diesel": diesel_points,
        "Gasoline": gasoline_points
    }

    # Sort body types by points in descending order
    sorted_body_types = sorted(
        body_type_points.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Sort fuel types by points in descending order
    sorted_fuel_types = sorted(
        fuel_type_points.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Get the top two body types
    top_body_types = [k for k, v in sorted_body_types[:2]]

    # Get the top two fuel types
    top_fuel_types = [k for k, v in sorted_fuel_types[:2]]

    # Get descriptions for the top body types and fuel types
    body_descriptions = {body: BODY_TYPE_DESCRIPTIONS[body] for body in top_body_types}
    fuel_descriptions = {fuel: FUEL_TYPE_DESCRIPTIONS[fuel] for fuel in top_fuel_types}

    return top_body_types, body_descriptions, top_fuel_types, fuel_descriptions

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user answers from the form
        answers = {
            "general": request.form.get("general"),
            "passenger": request.form.get("passenger"),
            "cargo": request.form.get("cargo"),
            "travel": request.form.get("travel"),
            "driving": request.form.get("driving"),
            "trip": request.form.get("trip"),
            "value": request.form.get("value"),
            "towing": request.form.get("towing"),
            "efficiency": request.form.get("efficiency"),
            "scenario": request.form.get("scenario"),
            "maneuverability": request.form.get("maneuverability"),
            "routine": request.form.get("routine"),
            "usability": request.form.get("usability"),
            "battery": request.form.get("battery"),
            "price": request.form.get("price"),
            "safety": request.form.get("safety"),
            "reliability": request.form.get("reliability"),
            "maintenance": request.form.get("maintenance"),
            "availability": request.form.get("availability"),
            "answer_charging_station": request.form.get("answer_charging_station"),
            "height": request.form.get("height"),
            "at_home_charging": request.form.get("at_home_charging")
        }

        # Calculate recommendations
        top_body_types, body_descriptions, top_fuel_types, fuel_descriptions = CarPick(answers)

        # Render the result page
        return render_template(
            "index.html",
            top_body_types=top_body_types,
            body_descriptions=body_descriptions,
            top_fuel_types=top_fuel_types,
            fuel_descriptions=fuel_descriptions,
            show_result=True
        )

    # Render the initial form page
    return render_template("index.html", show_result=False)

if __name__ == "__main__":
    app.run(debug=True)