import { write_signature } from './signature.js';

const host = window.location.hostname;
const domain = host.match(/\.([^.]+)\./)?.[1] || host.split('.')[0];
const excludedDomains = ["seniwave", "exposhow"];

if (excludedDomains.includes(domain)) {
    return;
}

write_signature();