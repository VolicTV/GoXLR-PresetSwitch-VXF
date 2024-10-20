import sys
import asyncio
import logging
from config import USE_MOCK

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if USE_MOCK:
    from mock_goxlr import GoXLR, EffectBankPreset
else:
    from goxlr import GoXLR
    try:
        from goxlr import EffectBankPreset
    except ImportError:
        # Fallback if EffectBankPreset is not available
        class EffectBankPreset:
            Preset6 = "Preset6"
        logger.warning("EffectBankPreset not found in goxlr module. Using fallback.")

async def main():
    xlr = None
    try:
        logger.debug("Attempting to create GoXLR object...")
        xlr = GoXLR()
        if xlr is None:
            logger.error("Failed to create GoXLR object. Make sure the device is connected and the GoXLR App is running.")
            return

        logger.info(f"GoXLR object created: {xlr}")
        logger.debug(f"Available methods and attributes: {dir(xlr)}")

        logger.debug("Attempting to open connection...")
        await xlr.open()
        logger.info("Connection opened successfully")
        
        await setPresetSqueaks(xlr)
    
        current_preset = await xlr.get_current_preset()
        logger.info(f'The current VFX preset is now: {current_preset}')
    
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        logger.error(f"Error type: {type(e)}")

    finally:
        if xlr is not None and hasattr(xlr, 'close'):
            try:
                await xlr.close()
                logger.info("Connection closed successfully")
            except Exception as e:
                logger.error(f"Error closing GoXLR: {e}", exc_info=True)

async def setPresetSqueaks(xlr):
    if hasattr(xlr, 'set_fx_enabled'):
        await xlr.set_fx_enabled(True)
    else:
        logger.warning("set_fx_enabled method not found")

    if hasattr(xlr, 'set_active_effect_preset'):
        await xlr.set_active_effect_preset(EffectBankPreset.Preset6)
    else:
        logger.warning("set_active_effect_preset method not found")

    # TODO: Add any additional settings for the "Squeaks" preset here

if __name__ == "__main__":
    asyncio.run(main())
