

Fri, 21 Nov 25

### Isidore Device Technical Overview

- Protocol-free encryption operating at data link layer (layer 2)
    
    - Encrypts raw frames/packets at red interface
        
    - Inherently interoperable with any network including SDA mesh
        
    - No dependency on routing, waveform specifics, or protocols
        
- Gen 3 modular system design
    
    - Core crypto boundary fully enclosed with anti-tamper, power filtering, EMI proof
        
    - Separate adapter/wrapper modules for different interfaces (USB-C, RS-422, Ethernet, etc.)
        
    - Connects via SIEM basic connectors
        
    - Target: stay within 10W system budget
        

### Encryption Architecture & Capabilities

- Not certificate-based system
    
    - No PKI/KMI infrastructure requirements
        
    - Uses ephemeral keys autonomously generated from true hardware entropy source
        
    - Integrating QRNG with Shannon entropy scale of 1
        
- Dual encryption process for fail-safe
    
    - First encryptor: AES-256 GCM with MLDSA
        
    - Second encryptor: additional layer
        
    - Galvanic isolation between encryptors and red/black sides
        
- Bookend solution - requires Isidore device on both ends
    
    - Cannot interoperate with HAPI devices or other systems
        
    - Described as “routable MACsec” but proprietary algorithm
        

### Space & Environmental Requirements

- Gen 3 incorporates radiation-tolerant components, thermal control, EMI shielding
    
- Modular architecture for multiple domains:
    
    - Space version: radiation-hardened components
        
    - Terrestrial version: standard components (cost savings)
        
- System-on-module (SoM) approach
    
    - RAD-tolerant SoM for space applications
        
    - Regular terrestrial SoM for ground use
        
    - Plugs onto carrier board for modularity
        
- Design ready to start, awaiting PDR/CDR approval
    
- Environmental testing (TID, tempest) planned post-design completion
    

### Security & Anti-Detection Features

- Protocol Free Encryption Engine (PFFE) - NSA patented technology
    
    - Completely encapsulates packets (header, payload, footer)
        
    - Removes all protocol metadata
        
    - Random padding makes identical packets appear different sizes
        
- Low probability detection/intercept capabilities
    
    - Galois Counter Mode ensures crypto looks different each transmission
        
    - Galvanic isolation reduces unintentional emissions
        
    - Mechanical shielding for RF signature reduction
        
- SmartBeam QRC wrapper (separate SBIR project)
    
    - AI-driven beamformer with direct RF sampling
        
    - Quantum-resistant cryptography integration
        
    - Modular design for various mission parameters
        

### Testing & Certification Approach

- Test equipment/harnesses include:
    
    - VLAN traffic simulation and testing tools
        
    - Firmware loader with image verification
        
    - Loopback module for red/black separation testing
        
    - Basic EMI testing equipment
        
- External testing through Dayton Brown laboratory for tempest testing
    
- FIPS Level 4 used as yardstick (acknowledged as “meaningless” for NSA certification)
    
- Plan: internal testing where possible, formal lab testing for requirements beyond capability
    

---

Chat with meeting transcript: [https://notes.granola.ai/t/d4cb853f-e25f-4673-8d26-05e1564037ba](https://notes.granola.ai/t/d4cb853f-e25f-4673-8d26-05e1564037ba)