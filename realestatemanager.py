class Property:
    def __init__(self, prop_id, address, rent):
        self.prop_id = prop_id
        self.address = address
        self.rent = rent
        self.is_leased = False
        self.tenant = None
    
    def lease_property(self, tenant):
        if not self.is_leased:
            self.is_leased = True
            self.tenant = tenant
            return True
        else:
            print(f"This property at {self.address} is already leased.")
            return False
    
    def end_lease(self):
        if self.is_leased:
            self.is_leased = False
            self.tenant = None
            print(f"Lease ended for the property at {self.address}.")
        else:
            print(f"No active lease for the property at {self.address}.")
    
    def __str__(self):
        return f"Property ID: {self.prop_id}\nAddress: {self.address}\nRent: {self.rent}\nLeased: {self.is_leased}\nTenant: {self.tenant}\n"


class Owner:
    def __init__(self, owner_id, name):
        self.owner_id = owner_id
        self.name = name
        self.properties = []
    
    def add_property(self, property):
        self.properties.append(property)
    
    def __str__(self):
        return f"Owner ID: {self.owner_id}\nName: {self.name}\nProperties owned: {len(self.properties)}"


class Tenant:
    def __init__(self, tenant_id, name):
        self.tenant_id = tenant_id
        self.name = name
    
    def __str__(self):
        return f"Tenant ID: {self.tenant_id}\nName: {self.name}"


class Lease:
    def __init__(self, property, tenant, start_date, end_date):
        self.property = property
        self.tenant = tenant
        self.start_date = start_date
        self.end_date = end_date
    
    def __str__(self):
        return f"Lease Details:\nProperty: {self.property.address}\nTenant: {self.tenant.name}\nLease Period: {self.start_date} to {self.end_date}"


# Example usage:
if __name__ == "__main__":
    # Create owner
    owner1 = Owner(1, "John Doe")

    # Create properties
    prop1 = Property(101, "123 Main St", 1500)
    prop2 = Property(102, "456 Elm St", 2000)

    # Add properties to owner
    owner1.add_property(prop1)
    owner1.add_property(prop2)

    # Create tenant
    tenant1 = Tenant(1, "Alice Smith")

    # Lease property to tenant
    prop1.lease_property(tenant1)
    
    # Create lease
    lease1 = Lease(prop1, tenant1, "2024-07-01", "2025-06-30")

    # Display information
    print("Owner Information:")
    print(owner1)
    
    print("\nProperty Information:")
    print(prop1)
    print(prop2)
    
    print("\nTenant Information:")
    print(tenant1)
    
    print("\nLease Information:")
    print(lease1)
