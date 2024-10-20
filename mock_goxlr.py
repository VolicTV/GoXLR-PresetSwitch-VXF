class GoXLR:
    async def open(self):
        print("Mock: GoXLR opened")

    async def close(self):
        print("Mock: GoXLR closed")

    async def set_fx_enabled(self, enabled):
        print(f"Mock: FX {'enabled' if enabled else 'disabled'}")

    async def set_active_effect_preset(self, preset):
        print(f"Mock: Set active effect preset to {preset}")

    async def get_current_preset(self):
        return "Mock Preset"

class EffectBankPreset:
    Preset6 = "Preset6"

# Add any other necessary mock classes or functions
