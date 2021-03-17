"""Sensor platform for City of Cape Town Loadshedding Interface."""
from .const import (
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    SENSOR,
)
from .entity import CoctEntity

async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([CoctZoneSensor(coordinator, entry)])

class CoctZoneSensor(CoctEntity):
    """City of Cape Town Zone Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_zone"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("zone")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON