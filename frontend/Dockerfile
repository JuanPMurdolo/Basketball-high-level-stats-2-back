# Usa una imagen oficial de Node.js como base
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Si usas Next.js para producción:
# RUN npm run build

# Si solo quieres desarrollo (hot reload):
CMD ["npm", "run", "dev"]

# Si quieres servir estático (Next.js/React build):
# FROM node:20-alpine AS runner
# WORKDIR /app
# COPY --from=builder /app ./
# EXPOSE 3000
# CMD ["npm", "run", "start"]