area($geometry) < 1000000 and
not intersects($geometry, collect_geometries(overlay_nearest('DATAZONES_REPAIRED', $geometry)))

