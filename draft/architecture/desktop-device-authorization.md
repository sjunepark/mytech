# Desktop Device Authorization

**Status:** Draft — owner review required  
**Initial evidence:** Creo

## Tentative preference

For a desktop application that delegates account approval to a browser,
separate the user-authenticated approval channel from the desktop polling
channel.

Issue the desktop a short-lived opaque secret and a browser approval location.
The signed-in browser approves or denies the pending device for its current
owner. The desktop polls with its own secret and receives typed protocol states
such as pending, denied, expired, or completed rather than relying on display
messages or treating every expected wait state as a server fault.

Raw device secrets and issued desktop tokens cross only the boundary that needs
them. Store hashes when later verification does not require the original value,
bind records to an owner and expiry, and make successful redemption one-time.
Do not expose raw credentials through owner-facing device lists; provide
metadata and explicit revocation instead.

Bound polling frequency and lifetime, make replay and concurrent redemption
behavior explicit, and preserve enough safe metadata for account review and
incident response.

## Why this is uncertain

The pattern is implemented in one product. It is not yet clear whether it is
the preferred default over an established device-authorization standard,
loopback redirect, custom URI scheme, or platform credential broker.

## Promotion questions

- When should a product use this pattern instead of a standard OAuth device
  flow or local redirect?
- Which desktop token material may the server retain, even as a hash?
- What are the required expiry, polling, session, and revocation guarantees?
- Must every issued desktop credential appear in an owner-visible device list?

## If accepted

Promote the channel separation, one-time secret handling, typed polling states,
and owner-scoped revocation rules. Keep route names, table shapes, and identity
provider choices project-specific.
