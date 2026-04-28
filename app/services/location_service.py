from app.models.locations import Location


def get_or_create_location(db, country, state, city):
    country = country.strip().lower()
    state = state.strip().lower() if state else None
    city = city.strip().lower() if city else None

    location = db.query(Location).filter_by(
        country=country,
        state=state,
        city=city
    ).first()

    if not location:
        location = Location(
            country=country,
            state=state,
            city=city
        )
        db.add(location)
        db.flush()

    return location