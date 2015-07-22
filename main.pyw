import json
import os
import sys

from PyQt4 import Qt, QtCore, QtGui, uic

# www.pathofexile.com/item-data/weapon
# from poe.trade source
items_types = {
    "Helmet":
        ["Aventail Helmet", "Barbute Helmet", "Battered Helm", "Bone Circlet", "Callous Mask", "Close Helmet", "Cone Helmet", "Crusader Helmet", "Deicide Mask", "Eternal Burgonet", "Ezomyte Burgonet", "Fencer Helm", "Festival Mask", "Fluted Bascinet", "Gilded Sallet", "Gladiator Helmet", "Golden Mask", "Golden Wreath", "Great Crown", "Great Helmet", "Harlequin Mask", "Hubris Circlet", "Hunter Hood", "Iron Circlet", "Iron Hat", "Iron Mask", "Lacquered Helmet", "Leather Cap", "Leather Hood", "Lion Pelt", "Lunaris Circlet", "Magistrate Crown", "Mind Cage", "Necromancer Circlet", "Nightmare Bascinet", "Noble Tricorne", "Pig-Faced Bascinet", "Plague Mask", "Praetor Crown", "Prophet Crown", "Raven Mask", "Reaver Helmet", "Regicide Mask", "Royal Burgonet", "Rusted Coif", "Sallet", "Samite Helmet", "Scare Mask", "Secutor Helm", "Siege Helmet", "Silken Hood", "Sinner Tricorne", "Solaris Circlet", "Soldier Helmet", "Steel Circlet", "Torture Cage", "Tribal Circlet", "Tricorne", "Ursine Pelt", "Vaal Mask", "Vine Circlet", "Visored Sallet", "Wolf Pelt", "Zealot Helmet"],
    "One Hand Axe":
        ["Arming Axe", "Boarding Axe", "Broad Axe", "Butcher Axe", "Ceremonial Axe", "Chest Splitter", "Cleaver", "Decorative Axe", "Engraved Hatchet", "Etched Hatchet", "Infernal Axe", "Jade Hatchet", "Jasper Axe", "Karui Axe", "Reaver Axe", "Royal Axe", "Runic Hatchet", "Rusted Hatchet", "Siege Axe", "Spectral Axe", "Tomahawk", "Vaal Hatchet", "War Axe", "Wraith Axe", "Wrist Chopper"],
    "Flask":
        ["Amethyst Flask", "Colossal Hybrid Flask", "Colossal Life Flask", "Colossal Mana Flask", "Diamond Flask", "Divine Life Flask", "Divine Mana Flask", "Eternal Life Flask", "Eternal Mana Flask", "Giant Life Flask", "Giant Mana Flask", "Grand Life Flask", "Grand Mana Flask", "Granite Flask", "Greater Life Flask", "Greater Mana Flask", "Hallowed Hybrid Flask", "Hallowed Life Flask", "Hallowed Mana Flask", "Jade Flask", "Large Hybrid Flask", "Large Life Flask", "Large Mana Flask", "Medium Hybrid Flask", "Medium Life Flask", "Medium Mana Flask", "Quartz Flask", "Quicksilver Flask", "Ruby Flask", "Sacred Hybrid Flask", "Sacred Life Flask", "Sacred Mana Flask", "Sanctified Life Flask", "Sanctified Mana Flask", "Sapphire Flask", "Small Hybrid Flask", "Small Life Flask", "Small Mana Flask", "Topaz Flask"],
    "Fishing Rods":
        ["Fishing Rod"],
    "One Hand Sword":
        ["Ancient Sword", "Antique Rapier", "Apex Rapier", "Baselard", "Basket Rapier", "Battered Foil", "Battle Sword", "Broad Sword", "Burnished Foil", "Copper Sword", "Corsair Sword", "Courtesan Sword", "Cutlass", "Dragonbone Rapier", "Dragoon Sword", "Dusk Blade", "Elder Sword", "Elegant Foil", "Elegant Sword", "Estoc", "Eternal Sword", "Fancy Foil", "Gemstone Sword", "Gladius", "Graceful Sword", "Grappler", "Harpy Rapier", "Hook Sword", "Jagged Foil", "Jewelled Foil", "Legion Sword", "Midnight Blade", "Pecoraro", "Primeval Rapier", "Rusted Spike", "Rusted Sword", "Sabre", "Serrated Foil", "Smallsword", "Spiraled Foil", "Tempered Foil", "Thorn Rapier", "Tiger Hook", "Twilight Blade", "Vaal Blade", "Vaal Rapier", "Variscite Blade", "War Sword", "Whalebone Rapier", "Wyrmbone Rapier"],
    "Claw":
        ["Awl", "Blinder", "Cat's Paw", "Double Claw", "Eagle Claw", "Eye Gouger", "Fright Claw", "Gemini Claw", "Gouger", "Great White Claw", "Gut Ripper", "Hellion's Paw", "Imperial Claw", "Nailed Fist", "Noble Claw", "Prehistoric Claw", "Sharktooth Claw", "Sparkling Claw", "Terror Claw", "Thresher Claw", "Throat Stabber", "Tiger's Paw", "Timeworn Claw", "Twin Claw", "Vaal Claw"],
    "Body Armour":
        ["Arena Plate", "Assassin's Garb", "Astral Plate", "Battle Lamellar", "Battle Plate", "Blood Raiment", "Bone Armour", "Bronze Plate", "Buckskin Tunic", "Cabalist Regalia", "Carnal Armour", "Chain Hauberk", "Chainmail Doublet", "Chainmail Tunic", "Chainmail Vest", "Chestplate", "Colosseum Plate", "Commander's Brigandine", "Conjurer's Vestment", "Conquest Chainmail", "Copper Plate", "Coronal Leather", "Crimson Raiment", "Crusader Chainmail", "Crusader Plate", "Crypt Armour", "Cutthroat's Garb", "Desert Brigandine", "Destiny Leather", "Destroyer Regalia", "Devout Chainmail", "Dragonscale Doublet", "Eelskin Tunic", "Elegant Ringmail", "Exquisite Leather", "Field Lamellar", "Frontier Leather", "Full Chainmail", "Full Dragonscale", "Full Leather", "Full Plate", "Full Ringmail", "Full Scale Armour", "Full Wyrmscale", "General's Brigandine", "Gladiator Plate", "Glorious Leather", "Glorious Plate", "Golden Plate", "Holy Chainmail", "Hussar Brigandine", "Infantry Brigandine", "Lacquered Garb", "Latticed Ringmail", "Light Brigandine", "Lordly Plate", "Loricated Ringmail", "Mage's Vestment", "Majestic Plate", "Necromancer Silks", "Occultist's Vestment", "Oiled Coat", "Oiled Vest", "Ornate Ringmail", "Padded Jacket", "Padded Vest", "Plate Vest", "Quilted Jacket", "Ringmail Coat", "Sacrificial Garb", "Sadist Garb", "Sage's Robe", "Saint's Hauberk", "Saintly Chainmail", "Savant's Robe", "Scale Doublet", "Scale Vest", "Scarlet Raiment", "Scholar's Robe", "Sentinel Jacket", "Shabby Jerkin", "Sharkskin Tunic", "Silk Robe", "Silken Garb", "Silken Vest", "Silken Wrap", "Simple Robe", "Sleek Coat", "Soldier's Brigandine", "Spidersilk Robe", "Strapped Leather", "Sun Leather", "Sun Plate", "Thief's Garb", "Triumphant Lamellar", "Vaal Regalia", "Varnished Coat", "War Plate", "Waxed Garb", "Widowsilk Robe", "Wild Leather", "Wyrmscale Doublet", "Zodiac Leather"],
    "Map":
        ["Academy Map", "Arachnid Nest Map", "Arcade Map", "Arid Lake Map", "Arsenal Map", "Bazaar Map", "Bog Map", "Canyon Map", "Catacomb Map", "Cells Map", "Cemetery Map", "Colonnade Map", "Courtyard Map", "Coves Map", "Crematorium Map", "Crypt Map", "Dark Forest Map", "Dry Peninsula", "Dry Peninsula Map", "Dry Woods Map", "Dunes Map", "Dungeon Map", "Ghetto Map", "Gorge Map", "Graveyard Map", "Grotto Map", "Jungle Valley Map", "Labyrinth Map", "Marsh Map", "Maze Map", "Mine Map", "Mountain Ledge Map", "Mud Geyser Map", "Museum Map", "Necropolis Map", "Orchard Map", "Overgrown Ruin Map", "Overgrown Shrine Map", "Palace Map", "Pier Map", "Plateau Map", "Precinct Map", "Promenade Map", "Reef Map", "Residence Map", "Sewer Map", "Shipyard Map", "Shore Map", "Shrine Map", "Spider Forest Map", "Spider Lair Map", "Springs Map", "Strand Map", "Subterranean Stream Map", "Temple Map", "Thicket Map", "Tomb Map", "Torture Chamber Map", "Tropical Island Map", "Tunnel Map", "Underground River Map", "Underground Sea Map", "Vaal Pyramid Map", "Villa Map", "Waste Pool Map", "Wharf Map"],
    "One Hand Mace":
        ["Ancestral Club", "Auric Mace", "Barbed Club", "Battle Hammer", "Behemoth Mace", "Bladed Mace", "Ceremonial Mace", "Dragon Mace", "Dream Mace", "Driftwood Club", "Flanged Mace", "Gavel", "Legion Hammer", "Nightmare Mace", "Ornate Mace", "Pernarch", "Petrified Club", "Phantom Mace", "Rock Breaker", "Spiked Club", "Stone Hammer", "Tenderizer", "Tribal Club", "War Hammer", "Wyrm Mace"],
    "Amulet":
        ["Agate Amulet", "Amber Amulet", "Citrine Amulet", "Coral Amulet", "Gold Amulet", "Jade Amulet", "Jet Amulet", "Lapis Amulet", "Onyx Amulet", "Paua Amulet", "Turquoise Amulet"],
    "Two Hand Mace":
        ["Brass Maul", "Colossus Mallet", "Coronal Maul", "Dread Maul", "Driftwood Maul", "Fright Maul", "Great Mallet", "Imperial Maul", "Jagged Maul", "Karui Maul", "Mallet", "Meatgrinder", "Morning Star", "Piledriver", "Plated Maul", "Sledgehammer", "Solar Maul", "Spiny Maul", "Steelhead", "Terror Maul", "Totemic Maul", "Tribal Maul"],
    "Sceptre":
        ["Abyssal Sceptre", "Blood Sceptre", "Bronze Sceptre", "Carnal Sceptre", "Crystal Sceptre", "Darkwood Sceptre", "Driftwood Sceptre", "Grinning Fetish", "Horned Sceptre", "Iron Sceptre", "Karui Sceptre", "Lead Sceptre", "Ochre Sceptre", "Opal Sceptre", "Platinum Sceptre", "Quartz Sceptre", "Ritual Sceptre", "Royal Sceptre", "Sambar Sceptre", "Sekhem", "Shadow Sceptre", "Stag Sceptre", "Tyrant's Sekhem", "Vaal Sceptre", "Void Sceptre"],
    "Two Hand Axe":
        ["Abyssal Axe", "Dagger Axe", "Despot Axe", "Double Axe", "Ezomyte Axe", "Fleshripper", "Gilded Axe", "Headsman Axe", "Jade Chopper", "Jasper Chopper", "Karui Chopper", "Labrys", "Noble Axe", "Poleaxe", "Shadow Axe", "Stone Axe", "Sundering Axe", "Talon Axe", "Timber Axe", "Vaal Axe", "Void Axe", "Woodsplitter"],
    "Gem":
        ["Abyssal Cry", "Added Chaos Damage", "Added Cold Damage", "Added Fire Damage", "Added Lightning Damage", "Additional Accuracy", "Anger", "Animate Guardian", "Animate Weapon", "Arc", "Arctic Armour", "Arctic Breath", "Assassin's Mark", "Ball Lightning", "Ball Lightning", "Barrage", "Bear Trap", "Blind", "Blink Arrow", "Block Chance Reduction", "Blood Magic", "Blood Rage", "Bloodlust", "Bone Offering", "Burning Arrow", "Cast On Critical Strike", "Cast on Death", "Cast on Melee Kill", "Cast when Damage Taken", "Cast when Stunned", "Chain", "Chance to Flee", "Chance to Ignite", "Clarity", "Cleave", "Cold Penetration", "Cold Snap", "Cold to Fire", "Concentrated Effect", "Conductivity", "Conversion Trap", "Convocation", "Critical Weakness", "Culling Strike", "Curse On Hit", "Cyclone", "Decoy Totem", "Desecrate", "Determination", "Detonate Dead", "Detonate Mines", "Devouring Totem", "Discharge", "Discipline", "Dominating Blow", "Double Strike", "Dual Strike", "Elemental Hit", "Elemental Proliferation", "Elemental Weakness", "Empower", "Endurance Charge on Melee Stun", "Enduring Cry", "Enfeeble", "Enhance", "Enlighten", "Ethereal Knives", "Explosive Arrow", "Faster Attacks", "Faster Casting", "Faster Projectiles", "Fire Nova Mine", "Fire Penetration", "Fire Trap", "Fireball", "Firestorm", "Flame Dash", "Flame Surge", "Flame Totem", "Flameblast", "Flammability", "Flesh Offering", "Flicker Strike", "Fork", "Fortify", "Freeze Mine", "Freezing Pulse", "Frenzy", "Frost Blades", "Frost Wall", "Frostbite", "Generosity", "Glacial Cascade", "Glacial Hammer", "Grace", "Greater Multiple Projectiles", "Ground Slam", "Haste", "Hatred", "Heavy Strike", "Herald of Ash", "Herald of Ice", "Herald of Thunder", "Hypothermia", "Ice Bite", "Ice Crash", "Ice Nova", "Ice Shot", "Ice Spear", "Immortal Call", "Incinerate", "Increased Area of Effect", "Increased Burning Damage", "Increased Critical Damage", "Increased Critical Strikes", "Increased Duration", "Infernal Blow", "Innervate", "Iron Grip", "Iron Will", "Item Quantity", "Item Rarity", "Kinetic Blast", "Knockback", "Leap Slam", "Less Duration", "Lesser Multiple Projectiles", "Life Gain on Hit", "Life Leech", "Lightning Arrow", "Lightning Penetration", "Lightning Strike", "Lightning Tendrils", "Lightning Trap", "Lightning Warp", "Magma Orb", "Mana Leech", "Melee Damage on Full Life", "Melee Physical Damage", "Melee Splash", "Minion Damage", "Minion Life", "Minion Speed", "Minion and Totem Elemental Resistance", "Mirror Arrow", "Molten Shell", "Molten Strike", "Multiple Traps", "Multistrike", "Phase Run", "Physical Projectile Attack Damage", "Physical to Lightning", "Pierce", "Poacher's Mark", "Point Blank", "Poison Arrow", "Portal", "Power Charge On Critical", "Power Siphon", "Projectile Weakness", "Puncture", "Punishment", "Purity", "Purity of Fire", "Purity of Ice", "Purity of Lightning", "Rain of Arrows", "Raise Spectre", "Raise Zombie", "Rallying Cry", "Ranged Attack Totem", "Reave", "Reckoning", "Reduced Mana", "Rejuvenation Totem", "Remote Mine", "Righteous Fire", "Riposte", "Searing Bond", "Shield Charge", "Shock Nova", "Shockwave Totem", "Slower Projectiles", "Smoke Mine", "Spark", "Spectral Throw", "Spell Echo", "Spell Totem", "Split Arrow", "Static Strike", "Storm Call", "Stun", "Summon Chaos Golem", "Summon Flame Golem", "Summon Ice Golem", "Summon Raging Spirit", "Summon Skeletons", "Sweep", "Tempest Shield", "Temporal Chains", "Tornado Shot", "Trap", "Trap and Mine Damage", "Vaal Arc", "Vaal Burning Arrow", "Vaal Clarity", "Vaal Cold Snap", "Vaal Cyclone", "Vaal Detonate Dead", "Vaal Discipline", "Vaal Double Strike", "Vaal Fireball", "Vaal Flameblast", "Vaal Glacial Hammer", "Vaal Grace", "Vaal Ground Slam", "Vaal Haste", "Vaal Ice Nova", "Vaal Immortal Call", "Vaal Lightning Strike", "Vaal Lightning Trap", "Vaal Lightning Warp", "Vaal Molten Shell", "Vaal Power Siphon", "Vaal Rain of Arrows", "Vaal Reave", "Vaal Righteous Fire", "Vaal Spark", "Vaal Spectral Throw", "Vaal Storm Call", "Vaal Summon Skeletons", "Vengeance", "Vigilant Strike", "Viper Strike", "Vitality", "Vulnerability", "Warlord's Mark", "Weapon Elemental Damage", "Whirling Blades", "Wild Strike", "Wrath"],
    "Two Hand Sword":
        ["Bastard Sword", "Butcher Sword", "Corroded Blade", "Curved Blade", "Engraved Greatsword", "Etched Greatsword", "Exquisite Blade", "Ezomyte Blade", "Footman Sword", "Headman's Sword", "Highland Blade", "Infernal Sword", "Lion Sword", "Lithe Blade", "Longsword", "Ornate Sword", "Reaver Sword", "Spectral Sword", "Tiger Sword", "Two-Handed Sword", "Vaal Greatsword", "Wraith Sword"],
    "Jewel":
        ["Cobalt Jewel", "Crimson Jewel", "Viridian Jewel"],
    "Bow":
        ["Assassin Bow", "Bone Bow", "Citadel Bow", "Composite Bow", "Compound Bow", "Crude Bow", "Death Bow", "Decimation Bow", "Decurve Bow", "Grove Bow", "Harbinger Bow", "Highborn Bow", "Imperial Bow", "Ivory Bow", "Long Bow", "Maraketh Bow", "Ranger Bow", "Recurve Bow", "Reflex Bow", "Royal Bow", "Short Bow", "Sniper Bow", "Spine Bow", "Steelwood Bow", "Thicket Bow"],
    "Gloves":
        ["Ambush Mitts", "Ancient Gauntlets", "Antique Gauntlets", "Arcanist Gloves", "Assassin's Mitts", "Bronze Gauntlets", "Bronzescale Gauntlets", "Carnal Mitts", "Chain Gloves", "Clasped Mitts", "Conjurer Gloves", "Crusader Gloves", "Deerskin Gloves", "Dragonscale Gauntlets", "Eelskin Gloves", "Embroidered Gloves", "Fishscale Gauntlets", "Goathide Gloves", "Golden Bracers", "Goliath Gauntlets", "Hydrascale Gauntlets", "Iron Gauntlets", "Ironscale Gauntlets", "Legion Gloves", "Mesh Gloves", "Murder Mitts", "Nubuck Gloves", "Plated Gauntlets", "Rawhide Gloves", "Ringmail Gloves", "Riveted Gloves", "Samite Gloves", "Satin Gloves", "Serpentscale Gauntlets", "Shagreen Gloves", "Sharkskin Gloves", "Silk Gloves", "Slink Gloves", "Soldier Gloves", "Sorcerer Gloves", "Stealth Gloves", "Steel Gauntlets", "Steelscale Gauntlets", "Strapped Mitts", "Titan Gauntlets", "Trapper Mitts", "Vaal Gauntlets", "Velvet Gloves", "Wool Gloves", "Wrapped Mitts", "Wyrmscale Gauntlets", "Zealot Gloves"],
    "Vaal Fragments":
        ["Mortal Grief", "Mortal Hope", "Mortal Ignorance", "Mortal Rage", "Sacrifice at Dawn", "Sacrifice at Dusk", "Sacrifice at Midnight", "Sacrifice at Noon"],
    "Quiver":
        ["Blunt Arrow Quiver", "Broadhead Arrow Quiver", "Conductive Quiver", "Cured Quiver", "Fire Arrow Quiver", "Heavy Quiver", "Light Quiver", "Penetrating Arrow Quiver", "Rugged Quiver", "Serrated Arrow Quiver", "Sharktooth Arrow Quiver", "Spike-Point Arrow Quiver", "Two-Point Arrow Quiver"],
    "Divination Card":
        ["Abandoned Wealth", "Birth of the Three", "Chaotic Disposition", "Coveted Possession", "Doedre's Madness", "Emperor's Luck", "Gemcutter's Promise", "Hope", "Humility", "Jack in the Box", "Lantador's Lost Love", "Lucky Connections", "Rain of Chaos", "The Artist", "The Avenger", "The Battle Born", "The Betrayal", "The Brittle Emperor", "The Carrion Crow", "The Cataclysm", "The Celestial Justicar", "The Chains that Bind", "The Dark Mage", "The Doctor", "The Drunken Aristocrat", "The Encroaching Darkness", "The Explorer", "The Feast", "The Fiend", "The Flora's Gift", "The Gambler", "The Gemcutter", "The Gladiator", "The Hermit", "The Hoarder", "The Hunger", "The Incantation", "The Inventor", "The King's Blade", "The King's Heart", "The Last One Standing", "The Lover", "The Metalsmith's Gift", "The One With All", "The Pack Leader", "The Pact", "The Poet", "The Queen", "The Road to Power", "The Scarred Meadow", "The Scholar", "The Siren", "The Spoiled Prince", "The Summoner", "The Sun", "The Union", "The Warden", "The Watcher", "The Wind", "The Wrath", "Three Faces in the Dark", "Time-Lost Relic", "Vinia's Token"],
    "Dagger":
        ["Ambusher", "Boot Blade", "Boot Knife", "Butcher Knife", "Carving Knife", "Copper Kris", "Demon Dagger", "Ezomyte Dagger", "Fiend Dagger", "Flaying Knife", "Glass Shank", "Golden Kris", "Gutting Knife", "Imp Dagger", "Imperial Skean", "Platinum Kris", "Poignard", "Prong Dagger", "Royal Skean", "Sai", "Skean", "Skinning Knife", "Slaughter Knife", "Stiletto", "Trisula"],
    "Shield":
        ["Alder Spike Shield", "Alloyed Spike Shield", "Ancient Spirit Shield", "Angelic Kite Shield", "Archon Kite Shield", "Baroque Round Shield", "Battle Buckler", "Bone Spirit Shield", "Branded Kite Shield", "Brass Spirit Shield", "Bronze Tower Shield", "Buckskin Tower Shield", "Burnished Spike Shield", "Cardinal Round Shield", "Cedar Tower Shield", "Ceremonial Kite Shield", "Champion Kite Shield", "Chiming Spirit Shield", "Colossal Tower Shield", "Compound Spiked Shield", "Copper Tower Shield", "Corroded Tower Shield", "Corrugated Buckler", "Crested Tower Shield", "Crimson Round Shield", "Crusader Buckler", "Driftwood Spiked Shield", "Ebony Tower Shield", "Elegant Round Shield", "Enameled Buckler", "Etched Kite Shield", "Ezomyte Spiked Shield", "Ezomyte Tower Shield", "Fir Round Shield", "Fossilized Spirit Shield", "Gilded Buckler", "Girded Tower Shield", "Goathide Buckler", "Golden Buckler", "Hammered Buckler", "Harmonic Spirit Shield", "Imperial Buckler", "Ironwood Buckler", "Ivory Spirit Shield", "Jingling Spirit Shield", "Lacewood Spirit Shield", "Lacquered Buckler", "Laminated Kite Shield", "Layered Kite Shield", "Linden Kite Shield", "Mahogany Tower Shield", "Maple Round Shield", "Mirrored Spiked Shield", "Mosaic Kite Shield", "Oak Buckler", "Ornate Spiked Shield", "Painted Buckler", "Painted Tower Shield", "Pine Buckler", "Pinnacle Tower Shield", "Plank Kite Shield", "Polished Spiked Shield", "Rawhide Tower Shield", "Redwood Spiked Shield", "Reinforced Kite Shield", "Reinforced Tower Shield", "Rotted Round Shield", "Scarlet Round Shield", "Shagreen Tower Shield", "Sovereign Spiked Shield", "Spiked Bundle", "Spiked Round Shield", "Spiny Round Shield", "Splendid Round Shield", "Splintered Tower Shield", "Steel Kite Shield", "Studded Round Shield", "Supreme Spiked Shield", "Tarnished Spirit Shield", "Teak Round Shield", "Thorium Spirit Shield", "Titanium Spirit Shield", "Twig Spirit Shield", "Vaal Buckler", "Vaal Spirit Shield", "Walnut Spirit Shield", "War Buckler", "Yew Spirit Shield"],
    "Wand":
        ["Carved Wand", "Crystal Wand", "Demon's Horn", "Driftwood Wand", "Engraved Wand", "Faun's Horn", "Goat's Horn", "Heathen Wand", "Imbued Wand", "Omen Wand", "Opal Wand", "Pagan Wand", "Profane Wand", "Prophecy Wand", "Quartz Wand", "Sage Wand", "Serpent Wand", "Spiraled Wand", "Tornado Wand"],
    "Boots":
        ["Ambush Boots", "Ancient Greaves", "Antique Greaves", "Arcanist Slippers", "Assassin's Boots", "Bronzescale Boots", "Carnal Boots", "Chain Boots", "Clasped Boots", "Conjurer Boots", "Crusader Boots", "Deerskin Boots", "Dragonscale Boots", "Eelskin Boots", "Goathide Boots", "Golden Caligae", "Goliath Greaves", "Hydrascale Boots", "Iron Greaves", "Ironscale Boots", "Leatherscale Boots", "Legion Boots", "Mesh Boots", "Murder Boots", "Nubuck Boots", "Plated Greaves", "Rawhide Boots", "Reinforced Greaves", "Ringmail Boots", "Riveted Boots", "Samite Slippers", "Satin Slippers", "Scholar Boots", "Serpentscale Boots", "Shackled Boots", "Shagreen Boots", "Sharkskin Boots", "Silk Slippers", "Slink Boots", "Soldier Boots", "Sorcerer Boots", "Stealth Boots", "Steel Greaves", "Steelscale Boots", "Strapped Boots", "Titan Greaves", "Trapper Boots", "Vaal Greaves", "Velvet Slippers", "Wool Shoes", "Wrapped Boots", "Wyrmscale Boots", "Zealot Boots"],
    "Currency":
        ["Albino Rhoa Feather", "Armourer's Scrap", "Blacksmith's Whetstone", "Blessed Orb", "Cartographer's Chisel", "Chaos Orb", "Chromatic Orb", "Divine Orb", "Eternal Orb", "Exalted Orb", "Gemcutter's Prism", "Glassblower's Bauble", "Jeweller's Orb", "Mirror of Kalandra", "Orb of Alchemy", "Orb of Alteration", "Orb of Augmentation", "Orb of Chance", "Orb of Fusing", "Orb of Regret", "Orb of Scouring", "Orb of Transmutation", "Portal Scroll", "Regal Orb", "Scroll of Wisdom", "Vaal Orb"],
    "Ring":
        ["Amethyst Ring", "Coral Ring", "Diamond Ring", "Gold Ring", "Golden Hoop", "Iron Ring", "Moonstone Ring", "Paua Ring", "Prismatic Ring", "Ruby Ring", "Sapphire Ring", "Topaz Ring", "Two-Stone Ring", "Unset Ring"],
    "Belt":
        ["Chain Belt", "Cloth Belt", "Golden Obi", "Heavy Belt", "Leather Belt", "Rustic Sash", "Studded Belt"],
    "Staff":
        ["Coiled Staff", "Crescent Staff", "Eclipse Staff", "Ezomyte Staff", "Foul Staff", "Gnarled Branch", "Highborn Staff", "Imperial Staff", "Iron Staff", "Judgement Staff", "Lathi", "Long Staff", "Maelstr\u00f6m Staff", "Military Staff", "Moon Staff", "Primitive Staff", "Primordial Staff", "Quarterstaff", "Royal Staff", "Serpentine Staff", "Vile Staff", "Woodful Staff"]
}


class PoEFilterGUI(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        uic.loadUi('filter_gui.ui', self)

        for k, v in items_types.items():
            self.cbBaseType.addItems(v)
        self.cbBaseType.setCurrentIndex(0)

        self.cbClassType.addItems(list(items_types.keys()))
        self.cbClassType.setCurrentIndex(0)

        self.filter = PoEFilter()

        self.btnLoad.clicked.connect(self.Load)
        self.btnSave.clicked.connect(self.Save)
        self.btnAdd.clicked.connect(self.Add)
        self.btnUpdate.clicked.connect(self.Update)
        self.btnDel.clicked.connect(self.Del)
        self.btnDo.clicked.connect(self.Generate)
        self.listItems.clicked.connect(self.LoadItem)
        self.btnAddClass.clicked.connect(
            lambda: self.AddClassType(self.cbClassType, self.edClassType)
        )
        self.btnAddType.clicked.connect(
            lambda: self.AddClassType(self.cbBaseType, self.edBaseType)
        )
        self.btnFind.clicked.connect(
            lambda: self.FindString(self.edFind.text())
        )
        self.btnFindNext.clicked.connect(
            lambda: self.textEdit.find(self.edFind.text())
        )
        self.btnSetTextColor.clicked.connect(
            lambda: self._customColorDlg(self.edFontColor)
        )
        self.btnSetBackgroundColor.clicked.connect(
            lambda: self._customColorDlg(self.edBackgroundColor)
        )
        self.btnSetBorderColor.clicked.connect(
            lambda: self._customColorDlg(self.edBorderColor)
        )

        if os.path.isfile('config.json') and os.path.getsize('config.json'):
            self.Config = json.load(open('config.json', 'r'))

            print('loading config.json file: ', self.Config)

            self.setGeometry(
                QtCore.QRect(
                    *self.Config['geo']
                )
            )

        else:
            print('There is no "config.json" file...')

            self.Config = {'path': os.path.expanduser(
                os.path.join(
                    '~',
                    'Documents',
                    'My Games',
                    'Path of Exile'
                )
            )}

            screen = QtGui.QDesktopWidget().screenGeometry()
            self.move(
                (screen.width() - self.width()) / 2,
                (screen.height() - self.height()) / 2,
            )

        if not os.path.exists(self.Config['path']):
            os.makedirs(self.Config['path'])

    def closeEvent(self, event):
        print('close event...')

        with open('config.json', 'w') as output:
            self.Config['geo'] = self.geometry().getRect()
            print('working with config.json file, ', self.Config)

            json.dump(
                self.Config,
                output
            )

    def _parseFields(self):
        what = dict()

        val = self.cbPlayAlert.currentText()
        if val:
            what['PlayAlertSound'] = '{} {}'.format(
                val,
                self.spVolume.value()
            )

        for k, v in {
            'ItemLevel': self.edItemLevel.text(),
            'DropLevel': self.edDropLevel.text(),
            'Quality': self.edQuality.text(),
            'Rarity': self.edRarity.text(),
            'Class': self.edClassType.text(),
            'BaseType': self.edBaseType.text(),
            'Sockets': self.edSockets.text(),
            'LinkedSockets': self.edLinkedSockets.text(),
            'SocketGroup': self.edSocketGroup.text(),
            'Height': self.edHeight.text(),
            'Width': self.edWidth.text(),
            'SetTextColor': self.edFontColor.text(),
            'SetBackgroundColor': self.edBackgroundColor.text(),
            'SetBorderColor': self.edBorderColor.text(),
            'Visible':
                ['Hide', '', 'Show'][self.cbVisible.checkState()]
        }.items():
            if v:
                what[k] = v

        return what

    def Load(self):
        import re

        fileName = QtGui.QFileDialog.getOpenFileName(
            self,
            'Load previusly *.json, *.filter filter',
            self.Config['path'],
            'PoE filter files (*.filter);; JSON file (*.json)'
        )

        if fileName == '':  # Cancel pressed

            return

        elif os.path.splitext(fileName)[1] == '.filter':

            tmp = []
            dtmp, comments = dict(), ''

            for i, line in enumerate(open(fileName, 'r'), start=1):

                if line.startswith('Show') or line.startswith('Hide'):

                    if dtmp:
                        dtmp['Comments'] = comments
                        tmp.append(dtmp)

                    dtmp, comments = dict(), ''

                    dtmp = {
                        'Visible': line.lstrip().rstrip()
                    }

                elif not line.startswith('#') and len(line.lstrip().rstrip()):

                    s = line.rstrip().split(maxsplit=1)
                    dtmp[s[0].lstrip()] = s[1]

                elif line.startswith('#') and not re.match('# \d+', line):

                    comments += line

            if dtmp:
                dtmp['Comments'] = comments
                tmp.append(dtmp)

            fileName = jsonFileName = fileName.split('.', maxsplit=1)[0] + '.json'
            poe = PoEFilter(tmp)
            poe.save(jsonFileName)

        self.edPath.setText(fileName)
        self.filter.load(fileName)

        self.listItems.clear()
        for i, el in enumerate(self.filter.Items, start=1):
            self.listItems.addItem(str(i))

    def Save(self):
        fileName = QtGui.QFileDialog.getSaveFileName(
            self,
            'Save filter as *.json',
            self.Config['path'],
            'JSON file (*.json)'
        )

        self.filter.save(fileName)

        if self.textEdit.toPlainText():
            with open(fileName.split('.', maxsplit=1)[0] + '.filter', 'w') as output:
                output.write(self.textEdit.toPlainText())

    def FindString(self, str):

        extraSelections = []

        if not self.textEdit.isReadOnly():

            self.textEdit.moveCursor(QtGui.QTextCursor.Start)

            while self.textEdit.find(str):

                extra = QtGui.QTextEdit.ExtraSelection()
                extra.format.setFontUnderline(True)
                extra.format.setUnderlineColor(QtCore.Qt.red)

                extra.cursor = self.textEdit.textCursor()
                extraSelections.append(extra)

            self.textEdit.moveCursor(QtGui.QTextCursor.Start)
            self.textEdit.find(str)

        self.textEdit.setExtraSelections(extraSelections)

    def Add(self):

        self.listItems.addItem(str(len(self.filter.Items) + 1))
        self.filter.append(self._parseFields())


    def Update(self):
        self.filter.Items[self.listItems.currentRow()] = self._parseFields()

    def Del(self):

        self.filter.delete(self.listItems.currentRow())

        self.listItems.clear()
        for i, el in enumerate(self.filter.Items, start=1):
            self.listItems.addItem(str(i))

    def AddClassType(self, sender, receiver):

        i = sender.currentText()
        if len(i.split()) > 1:
            i = '"{}"'.format(i)

        receiver.setText('{} {}'.format(
            receiver.text(),
            i
        ))

    def AddClass(self):
        self.AddClassType(self.cbClassType, self.edClassType)

    def AddType(self):
        self.AddClassType(self.cbBaseType, self.edBaseType)

    def LoadItem(self):

        def _colorBtn(btn, ed, item, field):

            if field in item.keys():
                ed.setText(item[field])

                rgba = item[field].split()

                if len(rgba) == 3:
                    R, G, B = map(int, rgba)
                elif len(rgba) == 4:
                    R, G, B, A = map(int, rgba)

                btn.setStyleSheet(
                    'background-color: rgba({}); color: {}'.format(
                        ', '.join(rgba),
                        'rgba({}, {}, {})'.format(255 - R, 255 - G, 255 - B)
                    )
                )

            else:
                ed.clear()
                btn.setStyleSheet('background-color: light gray; color: black')

        self.edItemLevel.clear()
        self.edDropLevel.clear()
        self.edQuality.clear()
        self.edRarity.clear()
        self.edClassType.clear()
        self.edBaseType.clear()
        self.edSockets.clear()
        self.edSocketGroup.clear()
        self.edLinkedSockets.clear()
        self.edHeight.clear()
        self.edWidth.clear()
        self.cbPlayAlert.setCurrentIndex(-1)
        self.spVolume.setValue(0)
        self.spFontSize.setValue(32)

        index = self.listItems.currentRow()
        item = self.filter.Items[index]

        self.FindString('# {}'.format(index + 1))

        if item['Visible'] == 'Show':
            self.cbVisible.setCheckState(2)
        else:
            self.cbVisible.setCheckState(0)

        if 'ItemLevel' in item.keys():
            self.edItemLevel.setText(item['ItemLevel'])
        if 'DropLevel' in item.keys():
            self.edDropLevel.setText(item['DropLevel'])
        if 'Quality' in item.keys():
            self.edQuality.setText(item['Quality'])
        if 'Rarity' in item.keys():
            self.edRarity.setText(item['Rarity'])
        if 'Class' in item.keys():
            self.edClassType.setText(item['Class'])
        if 'BaseType' in item.keys():
            self.edBaseType.setText(item['BaseType'])
        if 'Sockets' in item.keys():
            self.edSockets.setText(item['Sockets'])
        if 'SocketGroup' in item.keys():
            self.edSocketGroup.setText(item['SocketGroup'])
        if 'LinkedSockets' in item.keys():
            self.edLinkedSockets.setText(item['LinkedSockets'])
        if 'Height' in item.keys():
            self.edHeight.setText(item['Height'])
        if 'Width' in item.keys():
            self.edWidth.setText(item['Width'])

        if 'PlayAlertSound' in item.keys():
            self.cbPlayAlert.setCurrentIndex(int(item['PlayAlertSound'].split()[0]) - 1)
            if len(item['PlayAlertSound'].split()) > 1:
                self.spVolume.setValue(
                    int(item['PlayAlertSound'].split()[1])
                )

        if 'SetFontSize' in item.keys():
            self.spFontSize.setValue(int(item['SetFontSize']))

        _colorBtn(self.btnSetTextColor, self.edFontColor, item, 'SetTextColor')
        _colorBtn(self.btnSetBorderColor, self.edBorderColor, item, 'SetBorderColor')
        _colorBtn(self.btnSetBackgroundColor, self.edBackgroundColor, item, 'SetBackgroundColor')


    def _customColorDlg(self, ed):
        if ed.text():
            clr = QtGui.QColorDialog(
                QtGui.QColor(map(int, *ed.text().split())),
                self
            )
        else:
            clr = QtGui.QColorDialog(self)

        ed.setText(
            '{} {} {} {}'.format(
                *clr.getColor().getRgb()
            )
        )

    def Generate(self):
        self.textEdit.clear()
        self.textEdit.insertPlainText(str(self.filter))


class PoEFilter():

    def __init__(self, initItems=[]):

        self.Items = initItems

    def load(self, path=''):
        if os.path.isfile(path) and os.path.getsize(path):
            self.Items = json.load(open(path, 'r'))

    def save(self, path=''):
        with open(path, 'w') as output:
            json.dump(self.Items, output)

    def append(self, what):
        self.Items.append(what)

    def delete(self, index):
        del self.Items[index]

    def __repr__(self):
        str = ''

        for i, d in enumerate(self.Items, start=1):

            str += '# {}\n{}\n'.format(i, d['Visible'])

            if 'Comments' in d.keys():
                str += d['Comments']

            for k, v in sorted(d.items()):
                if k not in ['Visible', 'Comments']:
                    str += '    {} {}\n'.format(k, v)

        return str


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    win = PoEFilterGUI()
    win.show()

    sys.exit(app.exec_())
